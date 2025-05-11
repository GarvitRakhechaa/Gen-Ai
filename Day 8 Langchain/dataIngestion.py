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
# arxiv loader

from langchain_community.document_loaders import ArxivLoader
arxiv_loader = ArxivLoader(query="1706.03762" )
arxiv_documents = arxiv_loader.load()  #arxiv document
# print(arxiv_documents)

#------------------------------------------------------------------

#Wikipedia loader
from langchain_community.document_loaders import WikipediaLoader
wiki_loader = WikipediaLoader("Langchain")
wiki_documents = wiki_loader.load()  # wikipedia document
# print(wiki_documents)

#------------------------------------------------------------------

