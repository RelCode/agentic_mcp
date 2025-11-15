from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def make_llm():
    """Create an Azure OpenAI LLM instance using environment variables."""
    return AzureChatOpenAI(
        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key = f"{os.getenv('AZURE_OPENAI_KEY')}",
        api_version = "2025-01-01-preview",
        temperature = 0.0,
        max_tokens = 4096,
        verbose = True,
    )