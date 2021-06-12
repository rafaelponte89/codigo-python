from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
x=24
x=25

wordFile = urlopen('http://pythonscraping.com/pages'
                   '/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
