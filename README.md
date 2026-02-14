# End-to-End Medical RAG Assistant

A modern, high-performance Medical RAG (Retrieval-Augmented Generation) assistant that leverages a local LLM for secure and private health-related queries. Using a medical textbook as its knowledge base, it provides accurate, context-aware information through a visually stunning web interface.

## 🚀 Key Features

- **Local LLM Integration**: Uses **Ollama (llama3.2:1b)** for fast, local inference without external API costs.
- **RAG Pipeline**: Retrieves relevant medical context from a Pinecone vector store populated from a comprehensive medical PDF.
- **Modern UI**: A premium, "glassmorphism" styled chat interface built with HTML5, CSS3 (Inter fonts, sage palette), and jQuery.
- **Optimized Performance**: Fine-tuned chunking (1000 characters) and temperature settings (0.1) for high accuracy and low latency (~15s response time).

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Orchestration**: LangChain
- **LLM**: Ollama (llama3.2:1b)
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2 (via HuggingFace)
- **Vector Database**: Pinecone
- **Frontend**: HTML5, Vanilla CSS, jQuery

## 📋 Prerequisites

1.  **Ollama**: Install from [ollama.com](https://ollama.com/) and pull the model:
    ```bash
    ollama pull llama3.2:1b
    ```
2.  **Pinecone**: Create a free account and get your API key.

## 🔧 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ayushisharmaprofile/end-to-end-medical-rag-assistant.git
    cd end-to-end-medical-rag-assistant
    ```

2.  **Create a `.env` file**:
    ```env
    PINECONE_API_KEY=your_pinecone_api_key
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Index the Data**:
    Run the ingestion script to process the PDF in the `data/` folder and store embeddings in Pinecone:
    ```bash
    python -m src.store_index
    ```

## 🚀 Usage

Start the Flask application:
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:8080`.

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
