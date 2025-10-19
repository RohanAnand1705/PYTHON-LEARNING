# from PyPDF2 import PdfMerger

# merger= PdfMerger()
# pdfs= ["sample-local-pdf.pdf","sample.pdf","c4611_sample_explain.pdf"]
# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("Merged_output.pdf")
# merger.close()
# import os
# os.startfile("Merged_output.pdf")

from PyPDF2 import PdfReader
reader = PdfReader("sample.pdf")

from PyPDF2 import PdfWriter
writer= PdfWriter()
writer.add_page(reader.pages[0])
writer.encrypt(user_password="1234")
writer.write("Output.pdf")
writer.close()


import os
os.startfile("Output.pdf")