import re

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+.# ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_jd_skills(jd_text):
    """
    Extract ATOMIC skills from JD (not full sentences)
    """
    jd_text = normalize(jd_text)

    keywords = [
        "python", "sql", "machine learning", "nlp",
        "data analysis", "data handling", "communication",
        "collaboration", "teamwork", "statistics"
    ]

    skills = set()
    for k in keywords:
        if k in jd_text:
            skills.add(k)

    return skills


def compute_ats_score(job_description, resume_text):
    jd_skills = extract_jd_skills(job_description)
    resume_text = normalize(resume_text)

    matched = [s for s in jd_skills if s in resume_text]
    missing = [s for s in jd_skills if s not in resume_text]

    score = int((len(matched) / len(jd_skills)) * 100) if jd_skills else 0

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }
