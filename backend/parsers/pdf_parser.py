import PyPDF2
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except:
        pass
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