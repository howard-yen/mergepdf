import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import re

def merge(dir):
    writer = PdfFileWriter()
    for file in os.listdir(dir):
        if(file.endswith('.pdf')):
            print(str(file))
            print(str(dir + "\\" + file))
            reader = PdfFileReader(file)
            for page in range(reader.getNumPages()):
                writer.addPage(reader.getPage(page))


    with open(dir + "\\" + "mergedPDFs.pdf", "wb") as f:
        writer.write(f)

dir = input('Directory(empty for current): ')
if(dir == ''):
    dir = '.'

merge(dir)
print('---done---')