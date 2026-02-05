import streamlit as st
from utils import (
    extract_text,
    match_skills_dynamic,
    calculate_weighted_ats
)
from skills import extract_skills_from_jd, ROLE_PRIORITY_SKILLS

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Job Application Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🚀 Job Application Assistant")
st.markdown(
    "*ATS-style resume analyzer using Transformer-based semantic understanding*"
)

st.divider()

# -----------------------------------
# INPUT SECTION
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume (PDF / DOCX)",
        type=["pdf", "docx"]
    )

with col2:
    job_desc = st.text_area(
        "📋 Paste Company Job Description",
        height=180
    )

st.subheader("🎯 Role You're Applying For")

roles = [
    "ML Engineer",
    "Data Scientist",
    "Data Analyst",
    "Software Engineer",
    "Backend Developer",
    "Other"
]

selected_role = st.selectbox("Select role", roles)

custom_role = ""
if selected_role == "Other":
    custom_role = st.text_input("Enter custom role")

role = custom_role if selected_role == "Other" and custom_role else selected_role

analyze = st.button("🔍 Analyze Resume", type="primary")

# -----------------------------------
# MAIN LOGIC
# -----------------------------------

if analyze and resume_file and job_desc:

    with st.spinner("Analyzing resume using Transformer..."):

        # Resume text
        resume_text = extract_text(resume_file).lower()

        # 1️⃣ Extract skills dynamically from JD
        jd_skills = extract_skills_from_jd(job_desc)

        # Limit to top 10 skills (ATS behaviour)
        jd_skills = jd_skills[:10]

        # 2️⃣ Semantic matching
        found_skills, missing_skills = match_skills_dynamic(
            resume_text,
            jd_skills
        )

        # 3️⃣ Role-based weighting
        role_skills = ROLE_PRIORITY_SKILLS.get(role, [])

        ats_score = calculate_weighted_ats(
            found_skills,
            jd_skills,
            role_skills
        )

        # 4️⃣ Fresher normalization
        if ats_score < 40:
            ats_score += 20

        ats_score = min(ats_score, 100)

    # -----------------------------------
    # OUTPUT
    # -----------------------------------

    st.subheader("📊 ATS Compatibility Score")
    st.progress(ats_score / 100)
    st.metric("Final ATS Score", f"{ats_score}%")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Skills Matched")
        if found_skills:
            for skill in found_skills:
                st.success(skill)
        else:
            st.warning("No strong skill matches found")

    with col2:
        st.subheader("❌ Missing / Weak Skills")
        if missing_skills:
            for skill in missing_skills:
                st.error(f"Consider adding experience related to **{skill}**")
        else:
            st.success("Great match for this role!")

    st.divider()

    st.subheader("📝 Resume Improvement Suggestions")
    st.markdown(f"""
    - Customize your resume specifically for **{role}**
    - Align project descriptions with the job requirements
    - Highlight tools, frameworks, and technologies clearly
    - Quantify results (accuracy, performance, scale)
    - Mention internships, certifications, or hackathons
    """)

else:
    st.info("Upload resume and paste job description to begin.")
