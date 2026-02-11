from dotenv import load_dotenv
import os
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from pinecone import Pinecone 
pinecone_api_key = PINECONE_API_KEY

pc = Pinecone(api_key=pinecone_api_key)

from pinecone import ServerlessSpec 

index_name = "medical-chatbot"

# Check if the index exists and create it if necessary
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,  # Dimension of the embeddings
        metric="cosine",  # Cosine similarity
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Access the index after ensuring it exists
index = pc.Index(index_name)

from langchain_pinecone import PineconeVectorStore

# Load the existing Pinecone index
# Ensure the embedding and texts_chunk are defined elsewhere in the code
try:
    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embedding
    )
except NameError:
    raise NameError("Ensure 'embedding' is defined before using it to load the index.")