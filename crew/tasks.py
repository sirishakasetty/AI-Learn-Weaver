# crew/tasks.py
from crewai import Task
from crew.agents import summary_agent, example_agent, formatter_agent

summarization_task = Task(
    description="Summarize raw educational text into topic-based summary",
    expected_output="A structured summary of key concepts with headings and bullet points",
    agent=summary_agent
)

example_task = Task(
    description="Generate exam-style and real-world examples based on the summary",
    expected_output="List of examples and exercises aligned to each topic",
    agent=example_agent
)

formatting_task = Task(
    description="Format the summary and examples into a textbook or notebook layout",
    expected_output="Formatted text in textbook or notebook style depending on user choice",
    agent=formatter_agent
)
