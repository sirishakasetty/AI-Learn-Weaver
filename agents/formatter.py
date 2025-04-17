def format_summary(summary_text, output_format="textbook", grade_level="college"):
    """
    Format the summary based on user preferences:
    - output_format: 'textbook' or 'notebook'
    - grade_level: used to optionally simplify formatting
    """
    if output_format == "notebook":
        # Convert to bullet-point style with Q&A simplifications
        lines = summary_text.splitlines()
        formatted = ["📝 **Notebook Style Summary**\n"]
        for line in lines:
            line = line.strip()
            if line.startswith("**") or line.endswith(":"):
                formatted.append(f"📌 {line.strip('*:')}")
            elif line.startswith("-") or line.startswith("•"):
                formatted.append(f"  - {line.lstrip('-• ')}")
            elif line:
                formatted.append(f"  > {line}")
        return "\n".join(formatted)
    
    else:
        # Default: textbook layout
        formatted = (
            f"📘 **Textbook Style Chapter (Level: {grade_level})**\n\n"
            + summary_text
        )
        return formatted
