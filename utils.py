import pdfplumber
from docx import Document
from sentence_transformers import SentenceTransformer, util

# Load transformer model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text(file):
    if file.type == "application/pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""


def semantic_similarity(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).item()


def match_skills_dynamic(resume_text, jd_skills):
    """
    Match JD skills with resume using semantic similarity
    """
    matched, missing = [], []

    for skill in jd_skills:
        score = semantic_similarity(skill, resume_text)
        if score >= 0.25:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


def calculate_weighted_ats(found_skills, jd_skills, role_skills):
    """
    Role-aware ATS score
    """
    if not jd_skills:
        return 0

    score = 0
    max_score = len(jd_skills) + len(role_skills)

    for skill in found_skills:
        if skill in role_skills:
            score += 2   # role-critical skill
        else:
            score += 1   # normal JD skill

    return min(int((score / max_score) * 100), 100)
