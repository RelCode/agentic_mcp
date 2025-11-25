from typing import List, Dict, Any
from models import ExtractionResult

# for now we'll pretend as if anything from before 2020 is outdated
OUTDATED_YEAR_THRESHOLD = 2020

def verify_references(extraction: ExtractionResult) -> Dict[str, Any]:
    years = extraction.referenced_years or []
    potentially_outdated = [y for y in years if y < OUTDATED_YEAR_THRESHOLD]
    
    return {
        "potentially_outdated_references": potentially_outdated,
        "has_disclaimer": extraction.has_disclaimer,
        "has_scope_of_work": extraction.has_scope_of_work,
    }