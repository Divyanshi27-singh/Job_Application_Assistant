import streamlit as st
from utils import extract_text, match_skills_dynamic, calculate_weighted_ats
from skills import extract_skills_from_jd, ROLE_PRIORITY_SKILLS
from transformers import pipeline

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
    "*ATS-style resume analyzer with Transformer-based scoring and LLM-powered guidance*"
)

st.divider()

# -----------------------------------
# LOAD FREE LOCAL LLM
# -----------------------------------

@st.cache_resource
def load_llm():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

llm = load_llm()

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
# ATS ANALYSIS
# -----------------------------------

if analyze and resume_file and job_desc:

    with st.spinner("Running ATS analysis..."):

        resume_text = extract_text(resume_file).lower()
        jd_skills = extract_skills_from_jd(job_desc)[:10]

        found_skills, missing_skills = match_skills_dynamic(
            resume_text, jd_skills
        )

        role_skills = ROLE_PRIORITY_SKILLS.get(role, [])

        ats_score = calculate_weighted_ats(
            found_skills, jd_skills, role_skills
        )

        if ats_score < 40:
            ats_score += 20

        ats_score = min(ats_score, 100)

        st.session_state.ats_done = True
        st.session_state.ats_score = ats_score
        st.session_state.role = role
        st.session_state.found_skills = found_skills
        st.session_state.missing_skills = missing_skills

# -----------------------------------
# DISPLAY ATS RESULTS
# -----------------------------------

if st.session_state.get("ats_done", False):

    st.subheader("📊 ATS Compatibility Score")
    st.progress(st.session_state.ats_score / 100)
    st.metric("Final ATS Score", f"{st.session_state.ats_score}%")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Skills Matched")
        for s in st.session_state.found_skills:
            st.success(s)

    with col2:
        st.subheader("❌ Missing / Weak Skills")
        for s in st.session_state.missing_skills:
            st.error(s)

    st.divider()

    # -----------------------------------
    # 🤖 LLM CHATBOT (FIXED RESPONSE QUALITY)
    # -----------------------------------

    st.subheader("💬 Resume Assistant Chatbot")
    st.caption("Ask questions about your ATS score and resume improvements")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.chat_input(
        "Ask: How can I improve my ATS score?"
    )

    if user_question:

        prompt = f"""
You are an ATS resume expert.

STRICT RULES:
- Give ONLY ATS-related resume advice
- NO generic suggestions (do NOT say apply for jobs, gain experience, learn skills)
- Use the missing skills ONLY
- Give 3–4 bullet points
- Be practical and specific

ATS DETAILS:
Role: {st.session_state.role}
ATS Score: {st.session_state.ats_score}
Matched Skills: {', '.join(st.session_state.found_skills)}
Missing Skills: {', '.join(st.session_state.missing_skills)}

User Question:
{user_question}

Answer (bullet points only):
"""

        response = llm(
            prompt,
            max_length=200,
            do_sample=False
        )[0]["generated_text"].strip()

        if not response:
            response = (
                "• Add missing skills explicitly in your resume projects\n"
                "• Align project descriptions with job role requirements\n"
                "• Mention tools and technologies used for each project"
            )

        st.session_state.chat_history.append(("You", user_question))
        st.session_state.chat_history.append(("Assistant", response))

    for speaker, msg in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"**🧑 You:** {msg}")
        else:
            st.markdown(f"**🤖 Assistant:**\n{msg}")

else:
    st.info("Upload resume and paste job description to begin.")
