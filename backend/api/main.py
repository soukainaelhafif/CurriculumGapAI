from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from backend.parsers.pdf_parser import extract_text_from_pdf, extract_skills
from backend.nlp.skill_extractor import find_skill_gap, get_matching_skills, JOBMARKET_SKILLS
from backend.database import get_db, Analyse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "CurriculumGapAI läuft!"}

@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    text = extract_text_from_pdf(file.file)
    uni_skills = extract_skills(text)
    gap = find_skill_gap(uni_skills, JOBMARKET_SKILLS)
    matching = get_matching_skills(uni_skills, JOBMARKET_SKILLS)
    
    analyse = Analyse(
        datei_name=file.filename,
        fehlende_skills=gap,
        vorhandene_skills=matching
    )
    db.add(analyse)
    db.commit()

    return {
        "fehlende_skills": list(gap),
        "vorhandene_skills": list(matching)
    }

@app.get("/analysen")
def get_analysen(db: Session = Depends(get_db)):
    return db.query(Analyse).all()