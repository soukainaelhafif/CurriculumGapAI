import re
from backend.parsers.pdf_parser import extract_skills

JOBMARKET_SKILLS = [
    "Python", "Java", "JavaScript", "SQL", "PostgreSQL",
    "MongoDB", "Docker", "Kubernetes", "Git", "Linux",
    "Machine Learning", "Deep Learning", "TensorFlow",
    "React", "FastAPI", "AWS", "Azure", "CI/CD"
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