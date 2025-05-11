from langchain_community.document_loaders import TextLoader

loader = TextLoader("Phase 1 Foundations and Core Concep.txt")
# print(loader)
text_documents = loader.load()  # text document
print(text_documents)

#------------------------------------------------------------------


from langchain_community.document_loaders import PyPDFLoader

pdfloader = PyPDFLoader("tutorial.pdf")
pdf_documents = pdfloader.load()  # text document
print(pdf_documents)
#------------------------------------------------------------------