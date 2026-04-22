import re
from backend.parsers.pdf_parser import extract_skills

JOBMARKET_SKILLS = [
    # Programming Languages
    "Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "Go", "Rust", "Kotlin", "Swift",
    # Web Development
    "React", "Angular", "Vue", "Node.js", "FastAPI", "Django", "Spring Boot", "HTML", "CSS",
    # Data & AI
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn",
    "Computer Vision", "NLP", "LLM", "ChatGPT API",
    # Databases
    "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch",
    # DevOps & Cloud
    "Docker", "Kubernetes", "Git", "Linux", "AWS", "Azure", "Google Cloud", "CI/CD", "Jenkins",
    # Other
    "REST API", "GraphQL", "Microservices", "Agile", "Scrum"
]

def find_skill_gap(curriculum_skills, jobmarket_skills):
    curriculum_set = set(curriculum_skills)
    jobmarket_set  = set(jobmarket_skills)
    return jobmarket_set - curriculum_set

def get_matching_skills(curriculum_skills, jobmarket_skills):
    curriculum_set = set(curriculum_skills)
    jobmarket_set  = set(jobmarket_skills)
    return jobmarket_set & curriculum_set

# TEST
if __name__ == "__main__":
    uni_skills = ["Python", "Java", "SQL", "Algorithmen"]
    markt_skills = JOBMARKET_SKILLS
    
    gap = find_skill_gap(uni_skills, markt_skills)
    matching = get_matching_skills(uni_skills, markt_skills)
    
    print("Fehlende Skills:", gap)
    print("Vorhandene Skills:", matching)