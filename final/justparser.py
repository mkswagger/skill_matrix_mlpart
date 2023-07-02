file_name = "datsets\set3\Resume_12.pdf"
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import os
i_f = open(file_name, 'rb')
res_mgr = PDFResourceManager()
ret_data = io.StringIO()
txt_converter = TextConverter(res_mgr, ret_data, laparams=LAParams())
interpreter = PDFPageInterpreter(res_mgr, txt_converter)
for page in PDFPage.get_pages(i_f):
    interpreter.process_page(page)
    resume_text = ret_data.getvalue()
print(resume_text)