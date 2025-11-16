from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_llm():
    """Create an Azure OpenAI LLM instance using environment variables."""
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_KEY")
    
    if not deployment_name or not azure_endpoint or not api_key:
        raise ValueError("Azure OpenAI environment variables are not set properly.")
    
    return AzureChatOpenAI(
        deployment_name = deployment_name,
        azure_endpoint = azure_endpoint,
        api_key = api_key,
        api_version = "2025-01-01-preview",
        temperature = 0.0,
        max_tokens = 4096,
        verbose = True,
    )