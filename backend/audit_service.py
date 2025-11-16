from typing import Any, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from llm_client import get_llm

MOCK_DOCUMENT = """
This is a simple tax advisory letter regarding corporate tax compliance for the fiscal year 2022/2023.
It mentions Finance Act 2017 and does not clearly specify any disclaimer or scope of work.
"""

async def run_mock_audit() -> Dict[str, Any]:
    """
    Run mock audit on hardcoded document using LLM -- will later be replaced with real document processing.
    """
    llm = get_llm()
    prompt = ChatPromptTemplate.from_template(
        """
        You are an AI Document Auditor for tax and legal documents.

        You will be given the full text of a document. Your job is to:
            1. Identify any potential issues such as:
                - outdated references to legislation,
                - missing disclaimers,
                - missing scope of work,
                - unclear or risky language.
            2. Suggest improvements.
            3. Provide an overall risk score between 0 and 100 (higher = safer).

            Return your answer strictly as a JSON object with this structure:

            {{
            "issues": [
                {{
                "type": "string",
                "description": "string",
                "severity": "low|medium|high",
                "suggestion": "string"
                }}
            ],
            "overall_risk_score": 0,
            "summary": "string"
            }}

            Document to audit:
            ------------------
            {text}                                     
    """)
    
    parser = JsonOutputParser()
    
    messages = prompt.format_messages(text=MOCK_DOCUMENT)
    
    response = await llm.ainvoke(messages)
    
    try:
        parsed_output = parser.parse(response.content)
        return parsed_output
    except Exception as e:
        return {"error": f"Failed to parse LLM output: {str(e)}", "raw_output": response.content}