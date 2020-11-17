
import PyPDF2 

x = open('sample.pdf', 'rb') 
reader = PyPDF2.PdfFileReader(x) 
print(reader.numPages) 
pageObj = reader.getPage(0) 
print(pageObj.extractText())  
x.close()