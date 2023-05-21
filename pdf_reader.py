from PyPDF2 import PdfReader  # Library for reading PDF files

def read_pdf(pdf):
    """
    Function to read the text content of a PDF file.
    
    Parameters:
    pdf (stream): PDF file stream.

    Returns:
    text (str): String containing all the text from the PDF.
    """
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
