#Text Loader
from langchain_community.document_loaders import TextLoader

loader = TextLoader("Phase 1 Foundations and Core Concep.txt")
# print(loader)
text_documents = loader.load()  # text document
# print(text_documents)

#------------------------------------------------------------------
#pdf Loader

from langchain_community.document_loaders import PyPDFLoader

pdfloader = PyPDFLoader("tutorial.pdf")
pdf_documents = pdfloader.load()  # text document
# print(pdf_documents)
#------------------------------------------------------------------

#Web based loader
from langchain_community.document_loaders import WebBaseLoader

BaseLoader = WebBaseLoader("https://docs.chaicode.com/")
web_documents = BaseLoader.load()  # text document
# print(web_documents)

#------------------------------------------------------------------
 