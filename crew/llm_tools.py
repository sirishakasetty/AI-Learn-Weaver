from langchain_core.tools import tool
from llm.gemma_runner import generate_summary_with_gemma
from agents.example_generator import generate_examples_with_gemma
from agents.formatter import format_summary

@tool
def summarize_textbook(text: str, grade_level: str, output_format: str) -> str:
    """Summarizes text using Gemma into structured educational format."""
    return generate_summary_with_gemma(text, grade_level, output_format)

@tool
def generate_examples(summary: str, grade_level: str) -> str:
    """Creates examples or exercises from summarized content."""
    return generate_examples_with_gemma(summary, grade_level)

@tool
def format_content(summary: str, output_format: str, grade_level: str) -> str:
    """Formats summarized content into textbook or notebook format."""
    return format_summary(summary, output_format, grade_level)
