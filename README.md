The RAG-Based PDF Chatbot is an innovative tool that allows users to upload custom PDF documents and query their content through a conversational interface. Utilizing Retrieval-Augmented Generation (RAG), it integrates ChromaDB for vector storage and GPT-3.5 Turbo for language generation, built with Python and deployed via Streamlit.
Objectives
Enable dynamic PDF uploads and real-time querying.
Provide an interactive, context-aware chat experience.
Enhance usability with an attractive UI.
Technical Architecture
Frontend: Streamlit offers a user-friendly interface with a sidebar for uploads and a styled chat window.
Backend:
ingest.py extracts and chunks PDF text, creating embeddings stored in ChromaDB.
query.py uses RAG to retrieve and generate responses with GPT-3.5 Turbo.
Data: PDFs are saved in data/pdfs/, with vectors in data/chroma_db/. API keys are managed via .env or secrets.toml.
Dependencies: Includes streamlit, langchain, chromadb, and others from requirements.txt.
Features
Dynamic PDF upload (up to 200MB) with drag-and-drop support.
Real-time chat with styled messages and feedback spinners.
Attractive dark-themed UI with modern typography and interactive buttons.
Basic error handling for empty PDFs or processing issues.
Development Process
Initiated on August 22, 2025, the project evolved from a basic setup to a polished UI, resolving issues like empty embeddings with debugging. Tested with sample PDFs for accuracy.
Usage
Install dependencies with pip install -r requirements.txt.
Configure the OpenAI API key and run streamlit run app.py.
Upload PDFs and query via http://localhost:8501.
Future Improvements
Add images or animations to the UI.
Support multi-language queries.
Optimize for large PDF sets and explore cloud deployment.
Conclusion
As of 10:50 PM IST on August 22, 2025, the RAG-Based PDF Chatbot is a functional, user-friendly tool for PDF interaction, with ongoing plans for scalability and enhancements.
This concise version retains key details while fitting a shorter format. Let me know if further adjustments are needed!
