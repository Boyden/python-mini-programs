#merge pdf 
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))

path = "C:\\Users\\cole\\Desktop\\PDF"
os.chdir(path)
infnList = os.listdir(path)
merge_pdf(infnList, "C:\\Users\\cole\\Desktop\\linear_algebra.pdf")
