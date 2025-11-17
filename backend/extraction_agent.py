from typing import Any, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from llm_client import get_llm
from models import ExtractionResult

EXTRACTION_PROMPT = ChatPromptTemplate.from_template(
    """
        You are an assistant that extracts structured information from tax or legal advisory documents.

        Given the document text, identify:

            1. All referenced Acts or major pieces of legislation (as strings).
            2. All years mentioned that look like tax years or finance act years (as integers).
            3. Whether the document contains:
                - a disclaimer (about limitations/liability)
                - a clear scope of work (what is and is not covered).
            4. Any brief notes that might be relevant for an audit.

        Return ONLY a JSON object with this structure:

        {{
            "referenced_acts": ["string"],
            "referenced_years": [2021],
            "has_disclaimer": true,
            "has_scope_of_work": false,
            "notes": "optional string"
        }}

        Document:
        ---------
        {text}
        """
)

async def run_extraction_agent(document_text: str) -> ExtractionResult:
    llm = get_llm()
    parser = JsonOutputParser()
    
    messages = EXTRACTION_PROMPT.format_messages(text=document_text)
    
    response = await llm.ainvoke(messages)
    
    data: Dict[str, Any] = parser.parse(response.content)
    
    return ExtractionResult(**data)