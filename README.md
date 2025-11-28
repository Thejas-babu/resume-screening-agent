# 📄 AI Resume Screening Agent – Llama3 + Groq + Streamlit

This project automates the **resume screening process** using AI by comparing multiple candidate resumes against a given Job Description (JD) and ranking them based on fit.  
It helps recruiters, HR teams, and hiring managers quickly identify the most suitable candidates.

**Author:** Thejas Babu R

---

## 📌 Problem Statement

Manual resume screening is:

- Time-consuming ⏳  
- Prone to human bias 🧠  
- Hard to scale for large number of applicants 📈  

This project provides an **AI-powered solution** that:

- Reads and analyzes resumes (PDF/DOCX)  
- Compares them against the Job Description  
- Scores each candidate  
- Ranks them based on strengths, skills, and relevance  
- Exports a structured report  

---

## 🧠 Core Technologies

| Task | Technology Used |
|------|-----------------|
| AI Evaluation | Llama3 via Groq API |
| Web Interface | Streamlit |
| File Handling | Python, OS |
| Resume Parsing | PyPDF2, python-docx |
| Data Processing | Pandas |
| Deployment | Streamlit Cloud / Localhost |

---

## 📊 Features

- 📁 **Multi-Resume Upload** (PDF / DOCX)
- 🤖 **AI-Based Screening** using Llama3 (Groq)
- 🧮 **Candidate Scoring** (0–100)
- 🎯 **Fit Percentage** estimation
- ✅ **Decision Tagging** – Strong / Moderate / Weak fit
- 🧾 **Strengths & Weaknesses Summary**
- 📋 **Ranked Results Table**
- 📥 **CSV Report Download**
- 🎨 **Modern UI** with aesthetic dark-themed layout

---

## 🧪 Sample Workflow

1. **Paste Job Description** in the left panel (skills, tools, experience, responsibilities)
2. **Upload one or more resumes** (PDF/DOCX) in the right panel
3. Click on **🚀 Run Screening**
4. For each resume, the system will:
   - Extract text
   - Send content + JD to the AI model
   - Get back score, fit %, strengths, weaknesses, decision, and reasoning  
5. View the final **ranked candidate table**
6. **Download the results as CSV** for further analysis or sharing

---

## 📁 Project Structure

```bash
📂 resume-screening-agent/
├── agent.py              # Llama3 + Groq integration and screening logic
├── resume_parser.py      # PDF/DOCX parsing utilities
├── ranking.py            # Candidate scoring & sorting
├── streamlit_app.py      # Streamlit frontend (UI)
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore env, venv, caches
└── README.md             # Project documentation
🚀 Getting Started
🔹 Prerequisites
Python 3.8+

pip

Git

Groq API Key → https://console.groq.com

🔹 Installation
bash
Copy code
git clone https://github.com/Thejas-babu/resume-screening-agent.git
cd resume-screening-agent

python -m venv .venv
# Activate venv:
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt
🔹 Environment Setup
Create a .env file in the project root:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
⚠️ Do not commit .env to GitHub.
On Streamlit Cloud, put this key instead in Settings → Secrets.

🔹 Run the App Locally
bash
Copy code
streamlit run streamlit_app.py
Open in browser:
👉 http://localhost:8501

🌐 Deployment (Streamlit Cloud)
Push this project to GitHub

Go to https://share.streamlit.io

Create a new app, select your repo and streamlit_app.py as the main file

In App → Settings → Secrets, add:

env
Copy code
GROQ_API_KEY="your_groq_key_here"
Deploy and share the URL 🎉

👨‍💻 Contributors
Thejas Babu R – Developer

(Add more names if working as a team)

🧭 Future Enhancements
🧩 Skill-based matching using embeddings

📈 Analytics: charts for score distribution

🧾 Individual candidate PDF reports

🧪 ATS integration and resume parsing enhancements

🌐 Multi-language resume support

📜 License
This project is licensed under the MIT License – free to use, modify and distribute.
