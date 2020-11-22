import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import re

def merge(dir):
    merger = PdfFileMerger(strict=False)
    files = os.listdir(dir)
    files.sort()
    for file in files:
        if(file.endswith('.pdf')):
            print(str(file))
            merger.append(os.path.join(dir, file))

    with open(os.path.join(dir, "allLectures.pdf"), "wb") as f:
        merger.write(f)

if __name__ == "__main__":
    dir = input('Directory(empty for current): ')
    if(dir == ''):
        dir = os.getcwd()
    while(not os.path.exists(dir)):
        input("Directory not found, please try again: ")

    merge(dir)
    print('---done---')
