# 🚀 Job Application Assistant (ATS Resume Analyzer)

A Transformer-based Job Application Assistant that helps job seekers evaluate and improve their resumes against company-provided job descriptions, simulating how modern Applicant Tracking Systems (ATS) work.

Unlike traditional keyword-based systems, this project uses semantic understanding to analyze resumes, making the evaluation more realistic, explainable, and industry-relevant.

---

## 📌 Problem Statement

Many job applicants get rejected by ATS systems even when they have relevant skills, simply because their resumes are not aligned with specific job descriptions.

This project addresses that gap by:

- Comparing resumes directly against company job descriptions
- Identifying matched and missing skills
- Generating role-aware ATS compatibility scores
- Providing actionable, ATS-aligned resume improvement guidance

---

## 🎯 Target Users

- **Primary**: Job seekers (students, freshers, early professionals)
- **Secondary** (Future Scope): Recruiters for automated resume screening

---

## ✨ Key Features

- 📄 **Upload resumes** in PDF or DOCX format
- 📋 **Paste company job descriptions** (LinkedIn, career portals, etc.)
- 🎯 **Select the target job role**
- 🧠 **Dynamic skill extraction** from job descriptions
- 🔍 **Transformer-based semantic skill matching** using SentenceTransformers
- 📊 **Role-aware ATS compatibility scoring**
- ❌ **Identification of missing or weak skills**
- 💬 **LLM-powered resume assistant** for improvement guidance
- 🔒 **No paid or external APIs required** (offline & stable execution)

---

## 🧠 System Architecture & Technical Approach

### 1. Resume Parsing
Extracts clean text from PDF and DOCX resumes using `pdfplumber` and `python-docx`.

### 2. Dynamic Skill Extraction
Skills are derived directly from the job description using a comprehensive tech skill vocabulary. Avoids static or hardcoded skill lists.

### 3. Semantic Matching using Transformers
Uses `SentenceTransformer` (all-MiniLM-L6-v2) to capture semantic similarity, not just keywords.
- Example: "Flask service" ≈ "REST API deployment"

### 4. Role-Aware ATS Scoring
Applies role-specific skill weighting. Same resume can receive different ATS scores for different roles.

### 5. Fresher-Friendly Normalization
Prevents over-penalization of entry-level candidates. Adds bonus points to scores below 40% to make scoring more realistic for students and freshers.

### 6. LLM-Based Resume Assistant (Learning Application)
A lightweight LLM-powered assistant is integrated after ATS scoring using `google/flan-t5-base`. Generates human-readable explanations and guidance.

> ⚠️ **Core ATS logic remains deterministic** to avoid hallucination and ensure reliability. LLM is used only for explanation, not for decision-making.

---

## 🛠️ Tech Stack

| Technology------------|---------|
 | Purpose |
|| Python | Programming language |
| Streamlit | Interactive UI |
| SentenceTransformers | Semantic similarity |
| Transformers (Hugging Face) | LLM-based explanation layer |
| pdfplumber | PDF resume parsing |
| python-docx | DOCX resume parsing |

---

## 📁 Project Structure

```
JOB_APPLICATION_ASSISTANT/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── skills.py          # Skill extraction and role priorities
├── utils.py           # Resume parsing, semantic matching, ATS scoring
└── README.md          # This file
```

---

## ▶️ How to Run Locally

### 1. Clone the repository
```
bash
git clone <your-repo-url>
cd Job_Application_Assistant
```

### 2. Install dependencies
```
bash
pip install -r requirements.txt
```

### 3. Run the application
```
bash
streamlit run app.py
```

---

## 📊 Example Use Case

1. **Copy a job description** from LinkedIn or a company career page
2. **Upload your resume** (PDF or DOCX format)
3. **Select the role** you are applying for (ML Engineer, Data Scientist, Data Analyst, Software Engineer, Backend Developer, or Custom)
4. **View**:
   - 📊 ATS compatibility score
   - ✅ Matched skills
   - ❌ Missing skills
   - 💬 Resume improvement guidance from the LLM assistant

---

## 🔧 Supported Roles

- ML Engineer
- Data Scientist
- Data Analyst
- Software Engineer
- Backend Developer
- Custom (user-defined)

Each role has specific priority skills that are weighted more heavily in the ATS scoring algorithm.

---

## 🚀 Future Enhancements

- Section-wise ATS scoring (Skills / Projects / Experience)
- Advanced RAG-based resume coaching
- Resume bullet-point rewriting
- Recruiter-facing resume screening dashboard

---

## 📌 Key Learning Outcome

This project demonstrates:

- ✅ Practical application of Transformers for semantic matching
- ✅ Correct and responsible use of LLMs (as explanation layer only)
- ✅ Understanding of RAG-style workflows
- ✅ Industry-aligned system design decisions
- ✅ Building production-ready ML applications with Streamlit

---

## 📝 License

This project is for educational and personal use.

---

## 👤 Author

Created as a portfolio project demonstrating skills in:
- Natural Language Processing (NLP)
- Transformer Models
- Large Language Models (LLMs)
- Full-Stack ML Application Development
