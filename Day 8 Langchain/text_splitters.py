from langchain_community.document_loaders import PyPDFLoader

pdfloader = PyPDFLoader("tutorial.pdf")
pdf_documents = pdfloader.load()  # text document
# print(pdf_documents)

#how to recursively split text by characters

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

documents = text_splitter.split_documents(pdf_documents)
print("Splitted documents:")
print(documents[0].page_content)  # Print the content of the first split document