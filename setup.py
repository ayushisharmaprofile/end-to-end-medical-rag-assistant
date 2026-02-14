from setuptools import find_packages, setup 

setup(
    name="medical_rag", 
    version="0.1.0",
    author="AS",
    author_email="ayushisharma.profile@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain==0.3.0",
        "langchain-community==0.3.0",
        "langchain-core==0.3.0",
        "langchain-huggingface==0.1.0",
        "langchain-ollama==0.2.0",
        "langchain-pinecone==0.2.8",
        "langchain-text-splitters==0.3.0",
        "flask",
        "python-dotenv",
        "pypdf",
        "sentence-transformers",
        "pinecone"
    ]
)