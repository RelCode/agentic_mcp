from typing import List, Tuple
from models import AuditReport
from extraction_agent import run_extraction_agent
from auditing_agent import run_audit_agent

async def ochestrate_document_audit(document_text: str) -> Tuple[AuditReport, List[str]]:
    steps: List[str] = []
    
    steps.append("Step 1: Running Extraction Agent...")
    extraction = await run_extraction_agent(document_text)
    steps.append(f"Step 1 Completed: Extraction Result - {extraction}")
    steps.append("Step 2: Running Auditing Agent...")
    report = await run_audit_agent(document_text, extraction)
    steps.append("Step 2 Completed: Audit Report generated.")
    steps.append("Step 3: Generating Summary for Audit Report...")
    steps.append("Step 3 Completed: Summary generated.")
    return report, steps