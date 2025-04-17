# crew/crew_config.py
from crewai import Crew, Task
from crew.agents import summary_agent, example_agent, formatter_agent

# --- Define Tasks ---
summarization_task = Task(
    description="Summarize raw educational input into structured bullet/paragraph form",
    expected_output="A concise and structured summary with topic breakdowns",
    agent=summary_agent
)

example_task = Task(
    description="Generate relevant real-world and exam-style examples for each key topic",
    expected_output="Multiple examples for each section, in Q&A or problem format",
    agent=example_agent
)

formatting_task = Task(
    description="Format the summarized content + examples into textbook or notebook format",
    expected_output="Formatted content in Markdown style ready for rendering",
    agent=formatter_agent
)

# --- Create Crew ---
crew = Crew(
    agents=[summary_agent, example_agent, formatter_agent],
    tasks=[summarization_task, example_task, formatting_task],
    verbose=True
)

def run_crew_pipeline(raw_text: str, grade_level: str, output_format: str) -> str:
    # Feed inputs as memory variables to all tasks
    crew.context = {
        "text": raw_text,
        "grade_level": grade_level,
        "output_format": output_format
    }
    result = crew.run()
    return result
