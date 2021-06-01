import PyPDF2
file = input()
password = input()
pdf = open(file, "rb")
pdfReader = PyPDF2.PdfFileReader(pdf)
pdfWriter = PyPDF2.PdfFileWriter()

for p in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(p))
pdfWriter.encrypt(password)
result = open('encrypted.pdf', "wb")
pdfWriter.write(result)
result.close()