🚀 Job Application Assistant (ATS Resume Analyzer)

A Transformer-based Job Application Assistant that helps job seekers evaluate and improve their resumes against company-provided job descriptions, simulating how modern Applicant Tracking Systems (ATS) work.

Unlike traditional keyword-based systems, this project uses semantic understanding to analyze resumes, making the evaluation more realistic, explainable, and industry-relevant.



📌 Problem Statement

Many job applicants get rejected by ATS systems even when they have relevant skills, simply because their resumes are not aligned with specific job descriptions.

This project addresses that gap by:

Comparing resumes directly against company job descriptions

Identifying matched and missing skills

Generating role-aware ATS compatibility scores

Providing actionable, ATS-aligned resume improvement guidance



🎯 Target Users

Primary: Job seekers (students, freshers, early professionals)

Secondary (Future Scope): Recruiters for automated resume screening



✨ Key Features

Upload resumes in PDF or DOCX format

Paste company job descriptions (LinkedIn, career portals, etc.)

Select the target job role

Dynamic skill extraction from job descriptions

Transformer-based semantic skill matching

Role-aware ATS compatibility scoring

Identification of missing or weak skills

Resume improvement guidance

No paid or external APIs required (offline & stable execution)



🧠 System Architecture & Technical Approach
1. Resume Parsing

Extracts clean text from PDF and DOCX resumes

2. Dynamic Skill Extraction

Skills are derived directly from the job description

Avoids static or hardcoded skill lists

3. Semantic Matching using Transformers

Uses SentenceTransformer (all-MiniLM-L6-v2)

Captures semantic similarity, not just keywords

Example: “Flask service” ≈ “REST API deployment”

4. Role-Aware ATS Scoring

Applies role-specific skill weighting

Same resume can receive different ATS scores for different roles

5. Fresher-Friendly Normalization

Prevents over-penalization of entry-level candidates

Makes scoring more realistic for students and freshers

6. LLM-Based Resume Assistant (Learning Application)

A lightweight LLM-powered assistant is integrated after ATS scoring

Uses retrieved ATS analysis results as context (lightweight RAG-style flow)

Generates human-readable explanations and guidance

LLM is used only for explanation, not for decision-making

⚠️ Core ATS logic remains deterministic to avoid hallucination and ensure reliability.




🛠️ Tech Stack

Python

Streamlit – Interactive UI

SentenceTransformers – Semantic similarity

Transformers (Hugging Face) – LLM-based explanation layer

pdfplumber – PDF resume parsing

python-docx – DOCX resume parsing



▶️ How to Run Locally
1. Clone the repository
git clone <your-repo-url>
cd Job_Application_Assistant

2. Install dependencies
pip install -r requirements.txt

3. Run the application
streamlit run app.py



📊 Example Use Case

Copy a job description from LinkedIn or a company career page

Upload your resume

Select the role you are applying for

View:

ATS compatibility score

Matched skills

Missing skills

Resume improvement guidance



🚀 Future Enhancements

Section-wise ATS scoring (Skills / Projects / Experience)

Advanced RAG-based resume coaching

Resume bullet-point rewriting

Recruiter-facing resume screening dashboard



📌 Key Learning Outcome

This project demonstrates:

Practical application of Transformers

Correct and responsible use of LLMs

Understanding of RAG-style workflows

Industry-aligned system design decisions
