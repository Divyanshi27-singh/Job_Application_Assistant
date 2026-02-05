import re

# Universal skill vocabulary (only for detection)
COMMON_TECH_SKILLS = [
    "python", "java", "c++", "machine learning", "deep learning",
    "data analysis", "nlp", "computer vision",
    "tensorflow", "pytorch", "scikit-learn",
    "docker", "kubernetes", "mlops",
    "cloud", "aws", "gcp", "azure",
    "api", "rest api", "flask", "fastapi",
    "sql", "nosql", "mongodb", "postgresql",
    "data structures", "algorithms",
    "html", "css", "javascript", "react", "node.js",
    "statistics", "visualization", "excel"
]

# Role-specific important skills (for weighting)
ROLE_PRIORITY_SKILLS = {
    "ML Engineer": [
        "machine learning", "deep learning", "model deployment",
        "api", "flask", "fastapi", "docker"
    ],
    "Data Scientist": [
        "data analysis", "statistics", "machine learning",
        "pandas", "numpy", "visualization"
    ],
    "Data Analyst": [
        "sql", "data analysis", "excel",
        "pandas", "visualization"
    ],
    "Software Engineer": [
        "data structures", "algorithms",
        "api", "system design"
    ],
    "Backend Developer": [
        "api", "sql", "database",
        "flask", "fastapi"
    ]
}

def extract_skills_from_jd(jd_text):
    """
    Extract required skills dynamically from Job Description
    """
    jd_text = jd_text.lower()
    found = []

    for skill in COMMON_TECH_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, jd_text):
            found.append(skill)

    return list(set(found))
