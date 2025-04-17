import subprocess

def generate_summary_with_gemma(text, grade_level="Undergrad", output_format="textbook"):
    """
    Generate a structured chapter-style summary using Gemma LLM via Ollama.
    """

    # Safely truncate input to ~3900 characters to avoid LLM overload
    clean_text = text[:3900]

    prompt = f"""
You are a knowledgeable AI education assistant. Your task is to write a structured {output_format}-style educational summary for {grade_level} students based **only on the input content below**.

--- INSTRUCTIONS ---
• Use the content to extract the actual topic (e.g., Neural Networks, Climate Change, etc.).
• Write a clear and specific chapter title.
• Include a brief introduction to the topic.
• Present 3–5 key concepts as bullet points or sub-sections.
• Provide real-world examples or exercises related to the concepts.
• DO NOT generate content unrelated to the input.
• Stay strictly grounded in the transcript.

--- BEGIN TRANSCRIPT ---
{clean_text}
--- END TRANSCRIPT ---
"""

    result = subprocess.run(
        ["ollama", "run", "gemma:7b", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
