import asyncio
import pandas as pd
from uuid import uuid4
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Load environment variables from .env file
load_dotenv()


def load_excel_as_documents(file_path: str):
    """
    Read an Excel file and convert each row into a LangChain Document.

    Args:
        file_path (str): Path to the Excel file containing FAQs.

    Returns:
        List[Document]: List of LangChain documents.
    """
    df = pd.read_excel(file_path)

    documents = []
    for _, row in df.iterrows():
        content = f"Pertanyaan: {row['Question']}\nJawaban: {row['Answer']}"
        documents.append(Document(page_content=content))
    
    return documents


def init_google_embeddings():
    """
    Initialize Google embedding model with safe asyncio setup.

    Returns:
        GoogleGenerativeAIEmbeddings: Google embedding model instance.
    """
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")


def build_qa_chain(retriever, llm):
    """
    Construct a Retrieval-Augmented Generation QA chain.

    Args:
        retriever: The retriever to fetch relevant documents.
        llm: The language model to generate answers.

    Returns:
        QA chain (Runnable)
    """
    prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, document_chain)


def create_rag_chain(file_path: str = "data/FAQ_Nawa.xlsx"):
    """
    Set up the complete RAG (Retrieval-Augmented Generation) pipeline.

    Args:
        file_path (str): Path to the Excel file with QA data.

    Returns:
        RAG QA chain (Runnable)
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    embeddings = init_google_embeddings()

    # Initialize in-memory Qdrant vector store
    client = QdrantClient(":memory:")
    client.create_collection(
        collection_name="faq_qa",
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )

    vector_store = QdrantVectorStore(
        client=client,
        collection_name="faq_qa",
        embedding=embeddings,
    )

    # Load and store documents
    documents = load_excel_as_documents(file_path)
    ids = [str(uuid4()) for _ in documents]
    vector_store.add_documents(documents=documents, ids=ids)

    # Build and return the RAG chain
    retriever = vector_store.as_retriever()
    return build_qa_chain(retriever, llm)
