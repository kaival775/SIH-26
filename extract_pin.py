from docx import Document

doc = Document('C:/Users/khatr/Downloads/PINN.docx')

for page in doc.paragraphs:
    if page.page.n >= 5:
        break
    print(page.text)
