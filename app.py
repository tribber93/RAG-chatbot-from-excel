import streamlit as st
from dotenv import load_dotenv
from rag import create_rag_chain

# Load environment variables from .env file
load_dotenv()

qa_chain = create_rag_chain()

# Streamlit UI setup
st.set_page_config(page_title="Chatbot Gemini RAG", layout="centered")
st.title("💬 Chatbot Gemini + RAG")
st.caption("Ask anything related to the content in FAQ_Nawa.xlsx")

# Store chat history across interactions
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form for user message
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Anda:", placeholder="Enter your question here...")
    submitted = st.form_submit_button("Send")

# If user submitted a question
if submitted and user_input:
    st.session_state.chat_history.append(("Anda", user_input))  # Save user message

    # Get answer from the RAG chain
    result = qa_chain.invoke({"input": user_input})
    bot_reply = result.get("answer", "Sorry, I couldn't find an answer.")

    st.session_state.chat_history.append(("BOT", bot_reply))  # Save bot reply

# Display full chat history
for sender, message in st.session_state.chat_history:
    if sender == "Anda":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
