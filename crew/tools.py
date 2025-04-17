# crew/tools.py
from langchain_core.tools import tool
from agents.scraper import scrape_article_text
from agents.pdf_scraper import extract_text_from_pdf

@tool
def extract_article(link: str) -> str:
    """Extracts article content from a given URL."""
    return scrape_article_text(link)

@tool
def extract_pdf(path: str) -> str:
    """Extracts text from a local PDF file."""
    return extract_text_from_pdf(path)
