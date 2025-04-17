# crew/agents.py
from crewai import Agent
from tools.llm_tools import summarize_textbook, generate_examples, format_content

summary_agent = Agent(
    role="Summarizer Agent",
    goal="Summarize raw educational content into structured format",
    backstory="An expert at understanding large text passages and distilling them into key educational insights.",
    verbose=True,
    tools=[summarize_textbook]
)

example_agent = Agent(
    role="Example Generator Agent",
    goal="Generate real-world and exam-style examples based on summarized content",
    backstory="A highly creative agent trained to think in practical scenarios and student-style exercises.",
    verbose=True,
    tools=[generate_examples]
)

formatter_agent = Agent(
    role="Formatter Agent",
    goal="Convert raw content into textbook or notebook format",
    backstory="A formatting wizard who understands academic layouts and presentation styles for all grade levels.",
    verbose=True,
    tools=[format_content]
)
