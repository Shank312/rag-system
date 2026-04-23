# 🧠 Production-Ready RAG System (FastAPI + ChromaDB + LLMs)

> A scalable Retrieval-Augmented Generation (RAG) system designed to power real-world AI applications like documentation assistants, knowledge bots, and developer copilots.

🚀 Built for: AI Engineers, Backend Developers, and ML Practitioners

## 🏗️ Architecture

<img width="1536" height="1024" alt="01" src="https://github.com/user-attachments/assets/c73e0a82-66e6-4a1c-941e-87fc51a300c2" /><img width="5000" height="2812" alt="02" src="https://github.com/user-attachments/assets/5a2a4817-43d1-403d-b0ad-f8c8623b4230" /><img width="367" height="611" alt="03" src="https://github.com/user-attachments/assets/b15d46ad-35b8-44c2-b88f-9941fa3f6b2c" /><img width="705" height="851" alt="04" src="https://github.com/user-attachments/assets/2b717adc-ae5f-40eb-936b-17eb6fe2226f" /><img width="705" height="696" alt="05" src="https://github.com/user-attachments/assets/8223e91d-9937-4548-a011-889876886d53" /><img width="1376" height="684" alt="06" src="https://github.com/user-attachments/assets/a6f62e66-c9d8-43c1-8069-dadb432a28cf" /><img width="649" height="334" alt="07" src="https://github.com/user-attachments/assets/2eca33f2-3ff0-4b1b-b3ed-cc9b886f2e72" />

### Flow:
1. 📄 Documents → Chunked into smaller pieces
2. 🔢 Embeddings → Converted using embedding model
3. 🗄 Stored in ChromaDB (vector database)
4. 🔍 Query → Embedded & similarity searched
5. 🧠 Generator → LLM generates final answer using context


## 🎥 Demo

### Example Query:
"How are Iris models saved?"

### Response:
- Uses joblib for serialization
- Stored as `.pkl` file
- Retrieved via vector similarity search

📌 API Docs: http://127.0.0.1:8000/docs


## 💼 Use Cases

- 📚 Documentation Q&A (like ChatGPT for your docs)
- 👨‍💻 Developer Copilot for codebases
- 🧠 Research Assistant for PDFs & notes
- 🏢 Internal company knowledge chatbot


## 🚀 Why This Project?

Unlike basic chatbot demos, this system:

- Uses real retrieval (not hallucination)
- Supports scalable vector search
- Works with local + cloud LLMs
- Built with production-ready FastAPI backend


## 🔮 Roadmap

- [ ] Add streaming responses (OpenAI / SSE)
- [ ] Integrate LangChain / LlamaIndex
- [ ] Add hybrid search (BM25 + vector)
- [ ] UI with Streamlit / Next.js
- [ ] Docker deployment
- [ ] Authentication + multi-user support


## 👨‍💻 About Me

Hi, I'm Shankar Kumar — building production-level AI systems.

💡 Skills:
- AI/ML Systems
- RAG Pipelines
- FastAPI Backend
- Vector Databases

📬 Open for:
- Freelance AI projects
- Remote AI Engineer roles ($$$)

🔗 GitHub: https://github.com/Shank312











