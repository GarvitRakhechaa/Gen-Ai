from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyDFLoader

loader = TextLoader("Phase 1 Foundations and Core Concep.txt")
# print(loader)
text_documents = loader.load()  # text document
print(text_documents)


