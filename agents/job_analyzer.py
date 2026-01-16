from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
    streaming=False   # 🔒 ADD THIS
)


job_analyzer = Agent(
    role="Job Description Analyzer",
    goal="Analyze a job description and extract key skills and responsibilities",
    backstory="An expert HR analyst with years of experience screening resumes.",
    llm=llm,
    verbose=False,
    allow_delegation=False,   # ✅ ADD THIS
    max_iterations=1
)
