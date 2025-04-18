import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_examples_with_openai(summary, grade_level="Undergrad"):
    """
    Generate real-world and exam-style examples using OpenAI GPT.
    """
    prompt = f"""
You are an expert educational assistant. Based on the summary below, generate 3–5 practical and exam-style examples suited for {grade_level} students.

--- SUMMARY ---
{summary}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You generate practical examples for learning content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
