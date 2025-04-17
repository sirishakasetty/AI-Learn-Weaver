import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a local PDF file using PyMuPDF."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"Failed to extract PDF: {str(e)}"
