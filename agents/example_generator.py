# agents/example_generator.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_examples_with_openai(summary, grade_level="Undergrad"):
    prompt = f"""
You are an expert educator. Based on the following educational summary, generate 3–5 **exam-style questions or real-world examples** that help students at the {grade_level} level practice the topic.

--- SUMMARY ---
{summary}
--- END ---

Your output should be in plain text. Label the questions or examples clearly.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You generate practice questions and examples for students."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"].strip()
