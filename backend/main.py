from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from audit_service import run_mock_audit


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return { "status": "OK", "message": "Document Auditor Backend is running" }

@app.get("/audit/mock")
async def audit_mock():
    result = await run_mock_audit()
    return { "status": "OK", "result": result }

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return { "filename": file.filename, "content_type": file.content_type, "size": len(content) }