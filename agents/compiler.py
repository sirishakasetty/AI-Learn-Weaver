import os
import markdown2
from fpdf import FPDF

def compile_to_markdown(summary_text, examples_text, output_format="textbook", filename="output"):
    """
    Combines summary + examples into a markdown file.
    """
    combined = f"# AI-Generated {output_format.title()} \n\n"
    combined += summary_text + "\n\n"
    combined += "---\n\n"
    combined += "## ✍️ Practice Questions\n\n"
    combined += examples_text

    md_path = f"output/markdown/{filename}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(combined)

    return md_path


def convert_markdown_to_pdf(md_path, pdf_path=None):
    """
    Converts a markdown file to a simple PDF using FPDF.
    """
    if not pdf_path:
        pdf_path = md_path.replace("markdown", "pdf").replace(".md", ".pdf")

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown2.markdown(md_text)

    # Simple FPDF formatting
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

        # Basic rendering
    for line in html.splitlines():
        # Remove emojis and non-latin chars
        safe_line = ''.join(char if ord(char) < 128 else '?' for char in line)
        pdf.multi_cell(0, 10, safe_line)

    pdf.output(pdf_path)
    return pdf_path

