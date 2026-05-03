import PyPDF2

pdf_path = "Modul 11 - List Baru (1).pdf"
with open(pdf_path, 'rb') as file, open("pdf_output.txt", "w", encoding="utf-8") as out_file:
    reader = PyPDF2.PdfReader(file)
    for i, page in enumerate(reader.pages):
        out_file.write(f"--- Page {i+1} ---\n")
        out_file.write(page.extract_text() + "\n")
