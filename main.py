import os
from src.ingest import ingest_pdf
from src.query import load_vector_store, query_rag

def main():
    pdf_path = "Prompt Engineering_v4.pdf"  # Replace with your PDF name
    db_path = "chroma_db"  # Updated to Chroma persist directory
    
    # Step 1: Ingest PDF if DB doesn't exist
    if not os.path.exists(db_path):
        ingest_pdf(pdf_path, db_path)
    
    # Step 2: Load vector store
    vector_store = load_vector_store(db_path)
    
    # Step 3: Interactive chatbot loop
    print("Chatbot ready! Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == 'exit':
            break
        response, sources = query_rag(query, vector_store)
        print(f"Bot: {response}")
        print("Sources:")
        for i, doc in enumerate(sources):
            print(f"[{i+1}] {doc.page_content[:100]}... (Page {doc.metadata['page']})")

if __name__== "_main_":
    main()