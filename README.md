# 🎓 CurriculumGapAI

> AI-powered tool that analyzes university curricula and compares them to real job market demands — revealing the skill gaps students need to close.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.119-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-8.2-green)

---

## 🚀 What does it do?

Upload your university module handbook (PDF) and CurriculumGapAI will:

1. **Extract** all skills and topics from your curriculum
2. **Compare** them to current job market demands
3. **Show** exactly which skills you're missing
4. **Save** all analyses to a database for tracking

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| PDF Parser | pdfplumber, PyPDF2 |
| NLP | Custom skill extractor |
| Job Market Data | Adzuna API |
| Database SQL | PostgreSQL + SQLAlchemy |
| Database NoSQL | MongoDB + PyMongo |
| Frontend | HTML, CSS, JavaScript |

---

## 📊 Example Output

✅ Skills you already have: Python, Java, SQL
❌ Missing skills: Docker, AWS, React, Machine Learning...


---

## 🏃 How to run

```bash
# Clone the repository
git clone https://github.com/soukainaelhafif/CurriculumGapAI.git
cd CurriculumGapAI

# Install dependencies
pip install -r requirements.txt

# Start the server
python3 -m uvicorn backend.api.main:app --reload

# Open the app
open frontend/static/index.html
```

---

## 📁 Project Structure

CurriculumGapAI/
├── backend/
│   ├── api/          # FastAPI endpoints
│   ├── parsers/      # PDF extraction
│   ├── nlp/          # Skill analysis
│   ├── scraper/      # Job market data
│   └── database.py   # PostgreSQL connection
├── frontend/
│   └── static/       # HTML/CSS/JS
└── data/
├── raw/          # Uploaded PDFs
└── processed/    # Analysis results


---

## 👩‍💻 Built by

**Soukaina Elhafif**
Informatik Student @ h_da Darmstadt
[LinkedIn](https://www.linkedin.com/in/soukaina-elhafif/) | [GitHub](https://github.com/soukainaelhafif)

---


*Built as part of a BuildInPublic challenge — from idea to deployment in 7 days.*

## 💡 Why I built this

As a 5th semester Informatik student at h_da Darmstadt, I kept asking myself:
*"Am I learning the right things? Will my degree prepare me for the real job market?"*

So I built CurriculumGapAI to answer exactly that question — not just for me, 
but for every student who wonders the same thing.