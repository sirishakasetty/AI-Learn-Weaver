import re
import os

def classify_link(link):
    """Classifies a link as YouTube, article, or PDF."""
    youtube_pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/"
    article_pattern = r"(https?://)?(www\.)?.+\.(com|org|net|edu)(/.*)?"
    pdf_pattern = r"\.pdf$"

    if re.search(youtube_pattern, link):
        return "youtube"
    elif re.search(pdf_pattern, link) or link.lower().endswith(".pdf"):
        return "pdf"
    elif re.search(article_pattern, link):
        return "article"
    else:
        return "unsupported"

def classify_links(link_list):
    """Takes a list of links and returns a dictionary with classified types."""
    classified = {
        "youtube": [],
        "article": [],
        "pdf": [],
        "unsupported": []
    }

    for link in link_list:
        category = classify_link(link)
        classified[category].append(link)

    return classified
