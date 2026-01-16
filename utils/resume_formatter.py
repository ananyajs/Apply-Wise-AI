from utils.cleaner import clean_resume_text

def format_resume_pretty(
    raw_resume,
    name,
    city,
    phone,
    email,
    linkedin,
    university,
    graduation_year,
):
    body = clean_resume_text(raw_resume)

    header = f"""{name.upper()}
{city} | {phone} | {email} | {linkedin}
"""

    # REMOVE any AI-generated EDUCATION section
    body = body.split("EDUCATION")[0].strip()

    education = f"""
EDUCATION
B.Tech in Artificial Intelligence & Data Science
{university}
Expected Graduation: {graduation_year}
"""

    return f"{header}\n\n{body}\n\n{education}".strip()
