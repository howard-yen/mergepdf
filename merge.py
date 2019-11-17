import os
from PyPDF2 import PdfFileMerger

files = [f for f in os.listdir() if f.endswith(".pdf")]

merger = PdfFileMerger()

for f in files:
    merger.append(open(f, 'rb'))

with open("result.pdf", "wb") as fout:
    merger.write(fout)