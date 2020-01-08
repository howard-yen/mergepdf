import os
from PyPDF2 import PdfFileMerger
import re

def merge(dir):
    merger = PdfFileMerger()
    for file in os.listdir(dir):
        if(file.endswith('.pdf')):
            with open(dir + "\\" + file, 'rb') as f:
                merger.append(f)

    with open(dir + "\\" + "mergedPDFs.pdf", "wb") as f:
        merger.write(f)

dir = input('Directory(empty for current): ')
merge(dir)
