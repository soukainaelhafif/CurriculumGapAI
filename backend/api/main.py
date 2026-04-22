from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import traceback
from backend.parsers.pdf_parser import extract_text_from_pdf, extract_skills
from backend.nlp.skill_extractor import find_skill_gap, get_matching_skills, JOBMARKET_SKILLS


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "CurriculumGapAI läuft!"}

@app.post("/analyze")
async def analyze_pdf(file: UploadFile = File(...)):
    try:
        text = extract_text_from_pdf(file.file)
        uni_skills = extract_skills(text)
        gap = list(find_skill_gap(uni_skills, JOBMARKET_SKILLS))
        matching = list(get_matching_skills(uni_skills, JOBMARKET_SKILLS))

        try:
            from backend.database import get_db, Analyse
            db = next(get_db())
            analyse = Analyse(
                datei_name=file.filename,
                fehlende_skills=gap,
                vorhandene_skills=matching
            )
            db.add(analyse)
            db.commit()
            db.close()
        except:
            pass
            
        empfehlung = ""
        try:
            from backend.llm.recommendation import get_recommendation
            empfehlung = get_recommendation(gap, matching)
        except:
            pass

        return {
            "fehlende_skills": gap,
            "vorhandene_skills": matching,
            "empfehlung": empfehlung
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "trace": traceback.format_exc()}
        )

@app.get("/analysen")
def get_analysen():
    try:
        from backend.database import get_db, Analyse
        db = next(get_db())
        result = db.query(Analyse).all()
        db.close()
        return result
    except:
        return []