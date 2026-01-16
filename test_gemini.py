import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Test prompt
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Explain what a multi-agent AI system is in one clear sentence."
)


print(response.text)
