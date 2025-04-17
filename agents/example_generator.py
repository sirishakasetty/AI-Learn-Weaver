import subprocess

def generate_examples_with_gemma(topic_text, grade_level="college"):
    """
    Uses Gemma via Ollama to generate practical examples and questions.
    """
    prompt = f"""
You are an AI that creates practice content for students. Based on the topic below, generate the following for a {grade_level} level:

1. 2 Fill-in-the-blank questions
2. 2 Multiple-choice questions (with 4 options and correct answer)
3. 2 Conceptual questions for critical thinking

--- Topic Content ---
{topic_text}
"""

    result = subprocess.run(
        ["ollama", "run", "gemma:7b", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
