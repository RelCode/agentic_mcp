from orchestrator_agent import ochestrate_document_audit
from models import AuditReport

MOCK_DOCUMENT = """
This is a simple tax advisory letter regarding corporate tax compliance for the fiscal year 2022/2023.
It mentions Finance Act 2017 and does not clearly specify any disclaimer or scope of work.
"""

async def run_mock_audit() -> AuditReport:
    """
    Run mock audit on hardcoded document using LLM -- will later be replaced with real document processing.
    """
    report, _steps = await ochestrate_document_audit(MOCK_DOCUMENT)
    
    return report
    
async def run_text_audit(document_text: str) -> AuditReport:
    """
    Run audit on provided document text using LLM.
    """
    report, _steps = await ochestrate_document_audit(document_text)
    
    return report