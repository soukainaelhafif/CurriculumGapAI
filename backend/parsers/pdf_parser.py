import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Liest Text aus einer PDF Datei"""
    text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    
    return text

def extract_skills(text):
    """Findet Skills im Text"""
    
    skills = [
        "Python", "Java", "JavaScript", "SQL", "Machine Learning",
        "Deep Learning", "Docker", "Git", "React", "FastAPI",
        "TensorFlow", "PyTorch", "Pandas", "NumPy", "Linux"
    ]
    
    found_skills = []
    
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    
    return found_skills


# TEST
if __name__ == "__main__":
    print("PDF Parser bereit")
    print("Skills Liste:", ["Python", "Java", "SQL", "..."])