from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def save_resume_pdf(resume_text: str) -> str:
    file_path = "AI_Generated_Resume.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontSize = 10
    style.leading = 14

    elements = []
    for line in resume_text.split("\n"):
        elements.append(Paragraph(line.replace("&", "&amp;"), style))

    doc.build(elements)
    return file_path
