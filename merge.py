import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import re

def merge(dir):
    writer = PdfFileWriter()
    for file in os.listdir(dir):
        if(file.endswith('.pdf')):
            print(f'===adding {file}---')
            loc = os.path.join(dir, file)
            reader = PdfFileReader(loc)
            for page in range(reader.getNumPages()):
                writer.addPage(reader.getPage(page))

    with open(os.path.join(dir, 'merged.pdf'), "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    dir = input('Directory(empty for current): ')
    if(dir == ''):
        dir = os.getcwd()
    while(not os.path.exists(dir)):
        input("Directory not found, please try again: ")

    merge(dir)
    print('---done---')
