from setuptools import find_packages, setup

setup(
    name='CHATBOT-RAG',
    version='0.0.1',
    author='Ranjan Kumar',
    author_email='ranjan83711yadav@example.com',
    install_requires=[
        "openai",
        "langchain",
        "langchain-openai",
        "streamlit",
        "python-dotenv",
        "chromadb",
        "PyPDF2"
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)