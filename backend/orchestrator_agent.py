from models import AuditReport
from extraction_agent import run_extraction_agent
from auditing_agent import run_audit_agent

async def ochestrate_document_audit(document_text: str) -> AuditReport:
    extraction = await run_extraction_agent(document_text)
    report = await run_audit_agent(document_text, extraction)
    return report