from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from audit_service import run_mock_audit, run_text_audit
from pydantic import BaseModel
from orchestrator_agent import ochestrate_document_audit

app = FastAPI()
origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])

class TextAuditRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return { "status": "OK", "message": "Document Auditor Backend is running" }

@app.get("/audit/mock")
async def audit_mock():
    result = await run_mock_audit()
    return { "status": "OK", "result": result.model_dump() }

@app.post("/audit/text")
async def audit_text(payload: TextAuditRequest):
    print("Received audit text request", payload.text)
    result, steps = await ochestrate_document_audit(payload.text)
    return { 
            "status": "OK", 
            "result": result.model_dump(),
            "steps": steps
        }

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return { "filename": file.filename, "content_type": file.content_type, "size": len(content) }