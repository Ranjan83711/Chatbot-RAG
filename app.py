import streamlit as st
import os
from src.ingest import ingest_docs
from src.query import query_rag
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Custom CSS for a more attractive UI
st.markdown(
    """
    <style>
    .main {
        background-color: #1e1e2f;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stSidebar {
        background-color: #2c2c44;
        color: #e0e0e0;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #357abd;
        transform: scale(1.05);
    }
    .stTextInput>input {
        background-color: #33334d;
        color: #e0e0e0;
        border-radius: 10px;
        border: 1px solid #4a90e2;
    }
    .stChatMessage {
        background-color: #2c2c44;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .success-message {
        background-color: #28a745;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    .title {
        color: #4a90e2;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for chat history and vector store
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# Streamlit app layout with enhanced design
st.markdown('<div class="title">RAG-Based PDF Chatbot</div>', unsafe_allow_html=True)
st.markdown("Upload PDFs and ask questions about their content.", unsafe_allow_html=True)

# Sidebar for PDF upload with improved styling
with st.sidebar:
    st.markdown("<h2 style='color: #4a90e2; text-align: center;'>PDF Upload</h2>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Drag and drop files here", type="pdf", accept_multiple_files=True, help="Upload PDF files (max 200MB per file)")
    if uploaded_files:
        os.makedirs("data/pdfs", exist_ok=True)
        for uploaded_file in uploaded_files:
            with open(os.path.join("data/pdfs", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        st.markdown('<div class="success-message">PDFs uploaded successfully!</div>', unsafe_allow_html=True)
        
        with st.spinner("Processing PDFs..."):
            time.sleep(1)  # Simulate processing time for better UX
            st.session_state.vector_store = ingest_docs()
        if st.session_state.vector_store is None:
            st.warning("Failed to process PDFs. Check the console for errors and ensure PDFs are valid.")
        else:
            st.markdown('<div class="success-message">PDFs processed and vector store updated!</div>', unsafe_allow_html=True)

# Chat interface with styled messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

# User input with enhanced styling
if prompt := st.chat_input("Ask a question about the PDFs"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.vector_store:
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                time.sleep(1)  # Simulate response time for better UX
                response = query_rag(prompt, st.session_state.vector_store)
            st.markdown(response, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        with st.chat_message("assistant"):
            st.markdown("Please upload and process PDFs first.", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": "Please upload and process PDFs first."})