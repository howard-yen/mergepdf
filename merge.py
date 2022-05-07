import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
import re
import argparse

def merge(dir):
    merger = PdfFileMerger(strict=False)
    files = os.listdir(dir)
    files.sort()
    for file in files:
        if(file.endswith('.pdf')):
            print(str(file))
            merger.append(os.path.join(dir, file), import_bookmarks=False)

    with open(os.path.join(dir, "allLectures.pdf"), "wb") as f:
        merger.write(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge pdf files")
    parser.add_argument("--input_dir", type=str, help="Directory containing all the pdf files")
    args = parser.parse_args()
    if not os.path.exists(args.input_dir):
        raise Exception(f"input dir {args.input_dir} does not exist")

    merge(args.input_dir)
    print('---done---')
