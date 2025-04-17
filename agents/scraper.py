import yt_dlp
from newspaper import Article
import os

def scrape_youtube_transcript(url):
    """Download transcript text from a YouTube video using yt_dlp."""
    try:
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['en'],
            'subtitlesformat': 'vtt',
            'outtmpl': 'temp_youtube.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            subtitles = info.get("subtitles") or info.get("automatic_captions")
            if subtitles and "en" in subtitles:
                return f"Transcript available for: {url}"
            else:
                return "Transcript not available."
    except Exception as e:
        return f"Failed to extract YouTube transcript: {str(e)}"


def scrape_article_text(url):
    """Download and parse article text using newspaper3k."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Failed to scrape article: {str(e)}"
