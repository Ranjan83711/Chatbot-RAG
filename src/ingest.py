from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os
import glob

def ingest_docs():
    pdf_files = glob.glob("data/pdfs/*.pdf")
    documents = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(pdf_file)
        documents.extend(loader.load())
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(texts, embeddings, persist_directory="data/chroma_db")
    vector_store.persist()
    
    return vector_store