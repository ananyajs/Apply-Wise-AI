import re

def clean_resume_text(text: str) -> str:
    # Remove markdown
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"\|.*?\|", "", text)
    text = text.replace("*", "•")

    # REMOVE ANY PLACEHOLDERS LIKE [Candidate Name]
    text = re.sub(r"\[.*?\]", "", text)

    # Fix spacing
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
