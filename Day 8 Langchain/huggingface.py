import os
from dotenv import load_dotenv

load_dotenv("../.env")

HuggingFace_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
print(HuggingFace_API_KEY)

from langchain_huggingface import HuggingFaceEmbeddings

HuggingFace_enbeddings = HuggingFaceEmbeddings(
    model="all-MinLM-L6-v2",
)


text = "The quick brown fox jumps over the lazy dog."

query_result = HuggingFace_enbeddings.embed_query(text)
print(query_result)