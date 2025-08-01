# Gemini RAG Chatbot Nawatech

This chatbot uses Retrieval-Augmented Generation (RAG) technology with Google's Gemini model and Qdrant vector store. The chatbot can answer questions based on FAQ data stored in an Excel file.

## Features

- Streamlit-based chatbot with a simple UI.
- Uses LangChain for the RAG pipeline.
- Supports answer retrieval from FAQ data.
- Supports chat history storage.

## Folder Structure

```
RAG-chatbot-from-excel/
├── .venv/              # Virtual environment (optional)
├── data/
│   └── FAQ_Nawa.xlsx    # FAQ data (Excel)
├── .env                 # Environment variable file (API Key)
├── .env.example         # Example .env file
├── app.py               # Streamlit UI for the chatbot
├── rag.py               # RAG pipeline and utilities
├── Dockerfile           # Dockerfile for containerization
```

## Installation

1. **Clone the repository and enter the project folder:**

   ```bash
   git clone https://github.com/tribber93/RAG-chatbot-from-excel.git
   cd RAG-chatbot-from-excel
   ```

2. **Prepare the .env file with your API keys:**

   Copy the example file:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and fill in your API keys:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   LANGSMITH_API_KEY=your_langsmith_api_key_here
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Chatbot

```bash
streamlit run app.py
```

Access the chatbot via your browser at the address provided by Streamlit.

## Running with Docker

1. **Build the Docker image:**

   ```bash
   docker buildx build -t nawachatbot .
   ```

2. **Run the container:**

   ```bash
   docker run -p 8501:8501 nawachatbot
   ```

Access the chatbot via your browser at http://localhost:8501.

## How to Use

- Enter your question in the input field.
- The chatbot will answer based on the available FAQ data.
- Chat history will be displayed on the page.

## Configuration

- **API Key**: Store in the `.env` file
- **FAQ Data**: Store in `data/FAQ_Nawa.xlsx` with columns `Question` and `Answer`.

## Notes

- Make sure your Google and LangSmith API keys are valid.
