from io import BytesIO
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
# from audit_service import run_mock_audit, run_text_audit
from pydantic import BaseModel
from orchestrator_agent import orchestrate_document_audit
from pypdf import PdfReader

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
    # result = await run_mock_audit()
    # return { "status": "OK", "result": result.model_dump() }
    return { "status": "OK", "result": "Mock response" }

@app.post("/audit/text")
async def audit_text(payload: TextAuditRequest):
    print("Received audit text request", payload.text)
    extraction, result, steps, trace = await orchestrate_document_audit(payload.text)
    return { 
            "status": "OK", 
            "result": result.model_dump(),
            "steps": steps,
            "extraction": extraction.model_dump(),
            "trace": trace
        }
    
@app.post("/audit/file")
async def audit_file(file: UploadFile = File(...)):
    filename = file.filename.lower() if file.filename else ""
    if filename == "":
        return { "status": "Error", "message": "No filename provided." }
    
    try:
        # test file format using filename
        if filename.endswith(".txt"):
            # for now only support text files
            content_bytes = await file.read()
            text = content_bytes.decode('utf-8', errors='ignore')
            
        if filename.endswith(".pdf"):
            content_bytes = await file.read()
            pdf_reader = PdfReader(BytesIO(content_bytes))
            text = "\n".join(page.extract_text() or "" for page in pdf_reader.pages)
            
        else:
            return { "status": "Error", "message": "Unsupported file type. Only .txt and .pdf are supported." }
    except Exception as e:
        return { "status": "Error", "message": f"Failed to decode file content: {str(e)}" }
    
    print(text[:200])  # print first 200 chars for debugging
    
    extraction, report, steps, trace = await orchestrate_document_audit(text)
    return {
        "status": "OK",
        "filename": file.filename,
        "extracted_text_length": len(text),
        "result": report.model_dump(),
        "extraction": extraction.model_dump(),
        "steps": steps,
        "trace": trace
    }

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return { "filename": file.filename, "content_type": file.content_type, "size": len(content) }