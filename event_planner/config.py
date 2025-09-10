import os
from dotenv import load_dotenv
from smolagents import OpenAIServerModel

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = OpenAIServerModel(
    model_id="llama-3.1-8b-instant",
    api_base="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
)

LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")
