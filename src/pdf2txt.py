import pdfplumber

with pdfplumber.open(r'example.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
