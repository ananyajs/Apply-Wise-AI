from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
    streaming=False   # 🔒 ADD THIS
)


resume_agent = Agent(
    role="Resume Writer",
    goal="Create a concise, tailored resume based on job requirements",
    backstory="A professional resume writer who tailors resumes for ATS systems.",
    llm=llm,
    verbose=False,
    allow_delegation=False,   # ✅ ADD THIS
    max_iterations=1
)

