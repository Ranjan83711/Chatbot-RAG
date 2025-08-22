from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def query_rag(query, vector_store):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    result = qa_chain({"query": query})
    return result["result"]