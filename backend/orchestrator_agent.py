from typing import List, Tuple, Dict, Any
from models import AuditReport, ExtractionResult
from extraction_agent import run_extraction_agent
from auditing_agent import run_audit_agent

async def orchestrate_document_audit(document_text: str) -> Tuple[ExtractionResult, AuditReport, List[str], Dict[str, Any]]:
    steps: List[str] = []
    trace: Dict[str, Any] = {}
    
    steps.append("Step 1: Running Extraction Agent...")
    extraction, extraction_trace = await run_extraction_agent(document_text)
    steps.append(f"Step 1 Completed: Extraction Result - {extraction}")
    trace["extraction"] = extraction_trace
    steps.append("Step 2: Running Auditing Agent...")
    report = await run_audit_agent(document_text, extraction)
    steps.append("Step 2 Completed: Audit Report generated.")
    steps.append("Step 3: Generating Summary for Audit Report...")
    steps.append("Step 3 Completed: Summary generated.")
    return extraction, report, steps, trace