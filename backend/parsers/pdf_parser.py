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
       "Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "Go", "Rust", "Kotlin", "Swift",
        "React", "Angular", "Vue", "Node.js", "FastAPI", "Django", "Spring Boot", "HTML", "CSS",
        "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn",
        "Computer Vision", "NLP", "LLM", "ChatGPT API",
        "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch",
        "Docker", "Kubernetes", "Git", "Linux", "AWS", "Azure", "Google Cloud", "CI/CD", "Jenkins",
        "REST API", "GraphQL", "Microservices", "Agile", "Scrum"
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