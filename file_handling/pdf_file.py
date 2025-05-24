import PyPDF2 as pdf # pip install PyPDF2

with open(r'D:\Lessons.pdf','rb') as pdf_file:
    pdf_content = pdf.PdfReader(pdf_file)
    num_pages = len(pdf_content.pages)

    for i in range(num_pages):
        page = pdf_content.pages[i]
        text = page.extract_text()
        print(f"Page {i+1}: \n{text}")

