# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:22:57 2021

@author: Justin Platt
"""

import glob
import os
import pandas as pd
from pdfreader import PDFDocument, SimplePDFViewer
import PyPDF2
import re
from re import sub
import shutil
import sys
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    pdf_to_open = 'Test2.pdf'
    d_pdf = open(pdf_to_open, 'rb')  #open the file to be read by PyPDF2
    pdfReader = PyPDF2.PdfFileReader(d_pdf) #we'll use this to navigate the pdf
    viewer = SimplePDFViewer(d_pdf)
    viewer.render()
    print('|'.join(viewer.canvas.strings))
    #page_ct = pdfReader.getNumPages() #get number of pages
    #doc = PDFDocument(d_pdf)
    #catalog = doc.root
    #catalog.Pages[0].Contents.filter
    #print(f)
    #page_txt = pdfReader.getPage(0).extractText()
    #print(page_txt)

    


if __name__ == "__main__":
    main()
