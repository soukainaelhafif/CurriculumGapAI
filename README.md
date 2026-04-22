# 🎓 CurriculumGapAI

> AI-powered tool that analyzes university curricula and compares them to real job market demands — powered by OpenAI GPT.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)

---

## 🚀 What does it do?

Upload your university module handbook (PDF) and CurriculumGapAI will:

1. **Extract** all skills and topics from your curriculum using PyPDF2
2. **Compare** them to 50+ current job market skills
3. **Show** exactly which skills you're missing
4. **Recommend** what to learn next using OpenAI GPT
5. **Save** all analyses to PostgreSQL for tracking

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, FastAPI |
| PDF Parser | PyPDF2 |
| NLP | Custom skill extractor (50+ skills) |
| LLM | OpenAI GPT-3.5 Turbo |
| Job Market Data | Adzuna API |
| Database SQL | PostgreSQL + SQLAlchemy |
| Database NoSQL | MongoDB + PyMongo |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Railway (Backend) + GitHub Pages (Frontend) |
| CI/CD | GitHub Actions + pytest |

---

## 🌍 Live Demo

- **Frontend:** [soukainaelhafif.github.io/CurriculumGapAI](https://soukainaelhafif.github.io/CurriculumGapAI/)
- **API Docs:** [curriculumgapai-production.up.railway.app/docs](https://curriculumgapai-production.up.railway.app/docs)

---

## 🏃 How to run locally

```bash
git clone https://github.com/soukainaelhafif/CurriculumGapAI.git
cd CurriculumGapAI
pip install -r requirements.txt
uvicorn backend.api.main:app --reload
```

---

## 👩‍💻 Built by

**Soukaina Elhafif**
Informatik Student (5th Semester) @ h_da Darmstadt
[LinkedIn](https://www.linkedin.com/in/soukaina-elhafif/) | [GitHub](https://github.com/soukainaelhafif)

---

## 💡 Why I built this

As a 5th semester Informatik student at h_da Darmstadt, I kept asking myself:
*"Am I learning the right things? Will my degree prepare me for the real job market?"*

So I built CurriculumGapAI to answer exactly that question — not just for me, but for every student who wonders the same thing.
