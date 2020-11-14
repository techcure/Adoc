import json
import docx
import re
from docx import Document
import os

with open('serial.json', 'r') as json_file:
    js = json_file.read()

js = str(js)

# print(js)

parsed = json.loads(js)

text = json.dumps(parsed, indent=4)
# print(text)

# temp = re.search('', text).group()

new = text.replace('"', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace(',', '')
# print(new)

document = Document()
myfile = new
myfile = re.sub(r'[^\x00-\x7F]+|\x0c',' ', myfile) # remove all non-XML-compatible characters
p = document.add_paragraph(myfile)
document.save('file.docx')