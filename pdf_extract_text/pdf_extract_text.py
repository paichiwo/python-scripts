import PyPDF2

pdfFileObj = open('example.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# print the total number of pages in pdf
print(pdfReader.numPages)

# get a specific page of pdf by passing number since it stores pages in a list to access first page pass 0
pageObj = pdfReader.getPage(0)

# extract the page object by extractText() function
texts = pageObj.extractText()

print(texts)
