from PyPDF2 import PdfFileMerger
import sys

if len(sys.argv) > 1:
    pdfs = sys.argv[1:]
    merger = PdfFileMerger()
    
    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()

else:
    print('No PDF to merge.....')