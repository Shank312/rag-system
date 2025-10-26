# 🧠 RAG System (Retrieval-Augmented Generation)

A modular **Retrieval-Augmented Generation (RAG)** system built using **FastAPI**, **ChromaDB**, and **Python**.  
It retrieves relevant knowledge from markdown files and generates intelligent responses — designed for **AI/ML developers**, **engineers**, and **researchers**.

---

## 🚀 Features

✅ Retrieval-Augmented Question Answering (QA)  
✅ Persistent **Chroma Vector Database**  
✅ Modular architecture: `ingest`, `retriever`, `generator`  
✅ REST API powered by **FastAPI**  
✅ Supports **local & cloud deployment** (ngrok / Colab / server)  
✅ Easy integration with **Hugging Face** or **OpenAI** models  

---

## 🧩 Project Structure

rag-system/
│
├── app.py # Main FastAPI app
├── requirements.txt
├── .gitignore
│
├── src/
│ ├── init.py
│ ├── ingest.py # Handles knowledge ingestion into ChromaDB
│ ├── retriever.py # Fetches relevant chunks for queries
│ ├── generator.py # Generates final responses
│ └── app.py # (Optional) alternate app structure
│
├── data/
│ └── knowledge_base/ # Source knowledge files (.md)
│ ├── iris.md
│ ├── iris_project.md
│ ├── logger.md
│ ├── overview.md
│ └── project_overview.md
│
└── chromadb_store/ # Persistent ChromaDB (auto-generated)



---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shank312/rag-system.git
cd rag-system

2️⃣ Create a Virtual Environment

python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Linux/Mac)


3️⃣ Install Dependencies

pip install -r requirements.txt


🧠 Running the RAG System

🖥️ Local Development
uvicorn app:app --reload

Then open:
👉 Docs UI: http://127.0.0.1:8000/docs


☁️ Run in Google Colab (Optional)

If you want to test live in Colab, use:
!pip install pyngrok fastapi uvicorn nest_asyncio
from pyngrok import ngrok
import nest_asyncio, uvicorn
from app import app

nest_asyncio.apply()
public_url = ngrok.connect(8000).public_url
print("🌍 Public URL:", public_url)
uvicorn.run(app, host="0.0.0.0", port=8000)


🔍 API Usage
POST /query

Example Request:
curl -X POST "http://127.0.0.1:8000/query" \
     -H "Content-Type: application/json" \
     -d "{\"query\": \"How are Iris models saved?\"}"

Example Response:
{
  "query": "How are Iris models saved?",
  "answer": "Iris models are saved using joblib in the file iris_decision_tree_model.pkl",
  "retrieved": [
    "Iris project uses scikit-learn DecisionTree and joblib for persistence..."
  ]
}


🧱 Modules Overview:
| Module          | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| **`Ingestor`**  | Loads markdown knowledge files and stores embeddings in Chroma |
| **`Retriever`** | Finds most relevant chunks using cosine similarity             |
| **`Generator`** | Combines context and query to generate final answer            |
| **`app.py`**    | FastAPI interface exposing `/query` endpoint                   |


🧠 Future Enhancements

Integrate Hugging Face Transformers for local LLM generation

Add Streamlit UI for visual RAG exploration

Support multi-document upload and dynamic ingestion

Plug-in OpenAI GPT-4 API for enhanced generation


🧰 Tech Stack

| Layer       | Technology                      |
| ----------- | ------------------------------- |
| Backend     | FastAPI                         |
| Vector DB   | ChromaDB                        |
| Data        | Markdown Knowledge Base         |
| Optional ML | PyTorch / TensorFlow (optional) |
| Deployment  | ngrok / Uvicorn / Colab         |


🧑‍💻 Author

Shankar Kumar
🌐 GitHub

📘 AI/ML | System Design | Full-Stack Engineering


⭐ Contribute

Pull requests and feature suggestions are welcome!
If you find this helpful, please ⭐ the repo to show support.


📜 License

This project is open-source under the MIT License.


