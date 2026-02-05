# 🚀 Job Application Assistant (ATS Resume Analyzer)

A **Transformer-based Job Application Assistant** that helps job seekers evaluate and improve their resumes against **company-provided job descriptions**, simulating how modern **Applicant Tracking Systems (ATS)** work.

This project uses **semantic understanding** instead of simple keyword matching, making it more realistic and industry-relevant.

---

## 📌 Problem Statement
Many job applicants get rejected by ATS systems because their resumes do not align well with specific job descriptions, even when they have relevant experience.

This project solves that problem by:
- Comparing a resume directly against a company job description
- Identifying matched and missing skills
- Providing role-aware ATS compatibility scores
- Giving actionable resume improvement suggestions

---

## 🎯 Target Users
- **Primary:** Job seekers (students, freshers, early professionals)
- **Secondary (Future Scope):** Recruiters for resume screening

---

## ✨ Key Features
- Upload resume in **PDF or DOCX**
- Paste **company job description**
- Select the role you are applying for
- **Dynamic skill extraction** from job description
- **Transformer-based semantic skill matching**
- **Role-aware ATS compatibility score**
- Missing skills identification
- Resume improvement suggestions
- No external API required (offline & stable)

---

## 🧠 Technical Approach

### 1. Resume Parsing
- Extracts text from PDF and DOCX resumes

### 2. Dynamic Skill Extraction
- Skills are extracted directly from the job description
- No fixed or hardcoded skill list for scoring

### 3. Semantic Matching (Transformer)
- Uses **SentenceTransformer (all-MiniLM-L6-v2)**
- Captures semantic similarity (e.g., “Flask service” ≈ “REST API deployment”)

### 4. Role-Aware ATS Scoring
- Applies **role-specific skill weighting**
- Produces different scores for different roles using the same resume

### 5. Fresher-Friendly Normalization
- Avoids over-penalizing entry-level candidates

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (UI)
- **SentenceTransformers** (semantic similarity)
- **pdfplumber** (PDF parsing)
- **python-docx** (DOCX parsing)

---




---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd job-application-assistant



pip install -r requirements.txt

streamlit run app.py




📊 Example Use Case

Copy a job description from LinkedIn or a company website

Upload your resume

Select the role you are applying for

View ATS score, matched skills, missing skills, and improvement suggestions.
