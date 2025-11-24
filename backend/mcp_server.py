# import sys
# from pathlib import Path

from typing import Any, List
from mcp.server.fastmcp import FastMCP
# from mcp.types import CallToolResult, TextContext

# ROOT = Path(__file__).resolve().parents[1]
# sys.path.append(str(ROOT))

from models import Issue, AuditReport
from orchestrator_agent import orchestrate_document_audit

mcp = FastMCP("DocumentAuditorMCP")

@mcp.tool()
async def health_check() -> str:
    """
    Simple health check tool
    """
    return "Document Auditor MCP is healthy and running."

@mcp.tool()
async def extract_metadata(text: str) -> Any:
    """
    Extract structured metadata from tax/legal document text
    """
    extraction, _, _, _ = await orchestrate_document_audit(text)
    return {
        "referenced_acts": extraction.referenced_acts,
        "referenced_years": extraction.referenced_years,
        "has_disclaimer": extraction.has_disclaimer,
        "has_scope_of_work": extraction.has_scope_of_work,
        "notes": extraction.notes
    }

@mcp.tool()
async def audit_document_text(text: str) -> AuditReport:
    """
    Audit tax/legal document and return structured issues, score, summary & steps
    """
    print("We are in audit_document_text now")
    extraction, report, steps, trace = await orchestrate_document_audit(text)
    
    issues = [
        Issue(
            type=issue.type,
            description=issue.description,
            severity=issue.severity,
            suggestion=issue.suggestion
        )
        for issue in report.issues
    ]
    
    results = AuditReport(
        issues=issues,
        overall_risk_score=report.overall_risk_score,
        summary=report.summary,
        steps=steps
    )
    
    return results
    
if __name__ == "__main__":
    mcp.run()