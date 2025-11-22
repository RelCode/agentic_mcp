from typing import List, Optional
from pydantic import BaseModel

class Issue(BaseModel):
    type: str
    description: str
    severity: str # 'low', 'medium', 'high'
    suggestion: str
    
class ExtractionResult(BaseModel):
    referenced_acts: List[str]
    referenced_years: List[int]
    has_disclaimer: bool
    has_scope_of_work: bool
    notes: Optional[str] = None
    
class AuditReport(BaseModel):
    issues: List[Issue]
    overall_risk_score: int
    summary: str
    steps: List[str]