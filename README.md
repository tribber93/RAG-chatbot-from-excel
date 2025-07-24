# Chatbot Gemini RAG Nawatech

Chatbot ini menggunakan teknologi Retrieval-Augmented Generation (RAG) dengan model Gemini dari Google dan vektor store Qdrant. Chatbot dapat menjawab pertanyaan berdasarkan data FAQ yang disimpan dalam file Excel.

## Fitur

- Chatbot berbasis Streamlit dengan UI sederhana.
- Menggunakan LangChain untuk pipeline RAG.
- Mendukung pencarian jawaban dari data FAQ.
- Mendukung penyimpanan riwayat chat.

## Struktur Folder

```
RAG-chatbot-from-excel/
├── app.py               # Streamlit UI untuk chatbot
├── rag.py               # Pipeline RAG dan utilitas
├── data/
│   └── FAQ_Nawa.xlsx    # Data FAQ (Excel)
├── .env                 # File environment variable (API Key)
├── .env.example         # Contoh file .env
```

## Instalasi

1. **Clone repository dan masuk ke folder:**

   ```bash
   git clone <repo-url>
   cd case2
   ```

2. **Buat dan aktifkan virtual environment (opsional):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   _Jika belum ada `requirements.txt`, install manual:_

   ```bash
   pip install streamlit langchain langchain-google-genai langchain-qdrant qdrant-client python-dotenv pandas
   ```

4. **Siapkan file `.env`**

   - Copy `.env.example` menjadi `.env`
   - Isi dengan API key yang valid:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     LANGSMITH_API_KEY=your_langsmith_api_key_here
     ```

5. **Pastikan file FAQ_Nawa.xlsx sudah ada di folder `data/`**

## Menjalankan Chatbot

```bash
streamlit run app.py
```

Akses chatbot melalui browser di alamat yang diberikan oleh Streamlit.

## Cara Pakai

- Masukkan pertanyaan pada kolom input.
- Chatbot akan menjawab berdasarkan data FAQ yang tersedia.
- Riwayat chat akan ditampilkan di halaman.

## Konfigurasi

- **API Key**: Simpan di file `.env`
- **Data FAQ**: Simpan di `data/FAQ_Nawa.xlsx` dengan kolom `Question` dan `Answer`.

## Catatan

- Pastikan API key Google dan LangSmith valid.
