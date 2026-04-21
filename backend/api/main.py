from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.parsers.pdf_parser import extract_text_from_pdf, extract_skills
from backend.nlp.skill_extractor import find_skill_gap, get_matching_skills, JOBMARKET_SKILLS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "CurriculumGapAI läuft! 🚀"}

@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    uni_skills = extract_skills(text)
    gap = find_skill_gap(uni_skills, JOBMARKET_SKILLS)
    matching = get_matching_skills(uni_skills, JOBMARKET_SKILLS)
    
    return {
        "fehlende_skills": list(gap),
        "vorhandene_skills": list(matching)
    }