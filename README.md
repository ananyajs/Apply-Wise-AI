# 🤖 Multi-Agent AI Job Search Assistant

An intelligent multi-agent system that analyzes job descriptions, generates tailored resumes, computes JD match scores, and drafts recruiter outreach messages - all in one streamlined workflow.

---

## 🚀 Features

- 🧠 **Job Description Skill Extraction** – Identifies key technical and soft skills.
- 📄 **AI-Generated Resume** – Creates an ATS-friendly, tailored resume.
- 📊 **JD Match Score** – Provides a compatibility percentage with a skill gap breakdown.
- 💬 **Personalized Outreach** – Drafts recruiter / LinkedIn messages.
- 📥 **Resume Export** – Downloads the generated resume as a PDF.
- 🎯 **Multi-Agent Architecture** – Powered by CrewAI for collaborative task execution.

---

## 🧩 Architecture

- **Job Analyzer Agent**: Extracts required skills and responsibilities from the job description.
- **Resume Writer Agent**: Rewrites and tailors your profile into a clean one-page format.
- **Outreach Agent**: Drafts professional, high-conversion recruiter messages.
- **JD Match Scorer**: Computes the JD match score and identifies missing keywords.

---

## 🖥️ Demo Video

▶️ **Watch the full walkthrough here:** 👉 [Replace with your YouTube/Drive Link]

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI Framework)
- **CrewAI** (Multi-Agent Orchestration)
- **Google Gemini API** (LLM)
- **LangChain**
- **ReportLab** (PDF Generation)

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone [https://github.com/your-username/job_search_ai.git](https://github.com/your-username/job_search_ai.git)

# Navigate to project folder
cd job_search_ai

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```
---

## 📌 Use Cases

- Job Applications: Tailor applications quickly without manual editing.
-Resume Optimization: Ensure your resume passes through Applicant Tracking Systems (ATS).
-Recruiter Outreach: Automate the creation of personalized LinkedIn messages.

---

## 🙋‍♀️ Author

**Ananya JS**  
B.Tech in Artificial Intelligence & Data Science  
📍 Chennai, India  

🔗 **LinkedIn:** https://www.linkedin.com/in/ananyajs  

⭐ If you like this project, please give it a star!
