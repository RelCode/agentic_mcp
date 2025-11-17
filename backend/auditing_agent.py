from typing import List
from models import Issue, ExtractionResult, AuditReport
from tools_verification import verify_references
from langchain_core.prompts import ChatPromptTemplate
from llm_client import get_llm

SUMMARY_PROMPT = ChatPromptTemplate.from_template(
    """
        You are an AI Document Auditor.

        You will be given:
            - The document text.
            - A list of issues that were identified.
            - An overall risk score (0-100, higher = safer).

        Write a concise paragraph summarising:
            - What the document is about,
            - The key risks,
            - The main recommendations.

        Use a professional tone. Do not invent new issues; only rely on the provided list.

        Document:
        ---------
        {document_text}

        Issues:
        -------
        {issues_text}

        Overall risk score: {score}
    """
)

def build_issues_from_extraction (extraction: ExtractionResult, verification: dict) -> List[Issue]:
    issues: List[Issue] = []
    
    # check of outdated legilsation references
    if verification["potentially_outdated_references"]:
        issues.append(
            Issue(
                type="Outdate Legislation References",
                description=f"The document references potentially outdated legislation years: {verification['potentially_outdated_references']}.",
                severity="high",
                suggestion="Update references to the latest legislation where applicable."
            )
        )
        
    # check for missing disclaimer
    if not verification["has_disclaimer"]:
        issues.append(
            Issue(
                type="Missing Disclaimer",
                description="The document does not contain a disclaimer regarding limitations or liability.",
                severity="medium",
                suggestion="Include a clear disclaimer to limit liability."
            )
        )
        
    # check for missing scope of work
    if not verification["has_scope_of_work"]:
        issues.append(
            Issue(
                type="Missing Scope of Work",
                description="The document does not clearly define the scope of work.",
                severity="medium",
                suggestion="Define the scope of work to clarify what is and isn't covered."
            )
        )
        
    return issues

def calculate_risk_score (issues: List[Issue]) -> int:
    if not issues:
        return 90  # very safe if no issues
    
    score = 90
    for issue in issues:
        if issue.severity == "high":
            score -= 30
        elif issue.severity == "medium":
            score -= 15
        else:
            score -= 5
            
    return max(0, min(100, score))

async def run_audit_agent(document_text: str, extraction: ExtractionResult) -> AuditReport:
    verification = verify_references(extraction)
    issues = build_issues_from_extraction(extraction, verification)
    overall_risk_score = calculate_risk_score(issues)
    
    # use llm to summarize the findings
    llm = get_llm()
    issues_text = "\n".join(
        f"- [{i.severity.upper()}] {i.type}: {i.description} (Suggestion: {i.suggestion})"
        for i in issues
    ) or "No issues identified."
    
    messages = SUMMARY_PROMPT.format_messages(
        document_text=document_text,
        issues_text=issues_text,
        score=overall_risk_score
    )
    
    response = await llm.ainvoke(messages)
    summary = response.content.strip()
    
    
    return AuditReport(
        issues=issues,
        overall_risk_score=overall_risk_score,
        summary=summary
    )