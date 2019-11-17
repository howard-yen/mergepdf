import os
from PyPDF2 import PdfFileMerger
import re

def merge(dir):
    merger = PdfFileMerger()
    for f in os.listdir(dir):
        if(f.endswith('.pdf')):
            with open(f, 'rb') as f:
                merger.append(f)

    with open(dir + "mergedPDFs.pdf", "wb") as f:
        merger.write(f)

dir = input('Directory(empty for current): ')
merge(dir)
