from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
    streaming=False   # 🔒 ADD THIS
)


messaging_agent = Agent(
    role="Professional Outreach Writer",
    goal="Write concise, professional outreach messages for recruiters",
    backstory="An expert in professional communication.",
    llm=llm,
    verbose=False,
    allow_delegation=False,
    max_iterations=1   # 🔒 HARD STOP
)


