import PyPDF2

def extract_objects_from_pdf(pdf_file_path):
    pdf_objects = []
    
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page_objects = page.extract_text()  # Extract text from the page
            pdf_objects.append(page_objects)
    
    return pdf_objects

pdf_file_path = 'TCP1P-CTF.pdf'
extracted_objects = extract_objects_from_pdf(pdf_file_path)

# Print or process the extracted objects
for obj in extracted_objects:
    print(obj)
