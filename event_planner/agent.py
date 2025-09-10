from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    VisitWebpageTool,
    FinalAnswerTool,
)
from .tools import (
    search_event_venues,
    suggest_menu,
    catering_service_tool,
    SuperheroPartyThemeTool,
)
from .config import MODEL, LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST
import datetime
from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
import os

# importing credentials--------------
os.environ["LANGFUSE_PUBLIC_KEY"] = LANGFUSE_PUBLIC_KEY
os.environ["LANGFUSE_SECRET_KEY"] = LANGFUSE_SECRET_KEY
os.environ["LANGFUSE_HOST"] = LANGFUSE_HOST
# ----------------------------------


# Setting up langfuse------------------
langfuse = get_client()

# Verify connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")
# -----------------------------

# Starting instrument-------------------
SmolagentsInstrumentor().instrument()
# -----------------------------------


agent = CodeAgent(
    tools=[
        search_event_venues,  # already a Tool
        suggest_menu,  # already a Tool
        catering_service_tool,  # already a Tool
        VisitWebpageTool(),  # needs instantiation
        SuperheroPartyThemeTool(),  # needs instantiation
        FinalAnswerTool(),  # needs instantiation
        DuckDuckGoSearchTool(),  # needs instantiation
    ],
    model=MODEL,
    additional_authorized_imports=["datetime"],
    max_steps=10,
    verbosity_level=2,
)
