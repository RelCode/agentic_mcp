# import sys
# from pathlib import Path

from typing import Any
from mcp.server.fastmcp import FastMCP
# from mcp.types import CallToolResult, TextContext

# ROOT = Path(__file__).resolve().parents[1]
# sys.path.append(str(ROOT))

from models import Issue, AuditReport
from orchestrator_agent import orchestrate_document_audit

mcp = FastMCP("DocumentAuditorMCP")

@mcp.tool()
async def audit_document_text(text: str) -> dict:
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
    
    results = {
        "issues": issues,
        "overall_risk_score": report.overall_risk_score,
        "summary": report.summary,
        "steps": steps
    }
    
    return results
    
if __name__ == "__main__":
    mcp.run()