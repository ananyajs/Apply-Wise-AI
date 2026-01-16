import streamlit as st
import pandas as pd
from crew import run_job_search_ai
from utils.resume_formatter import format_resume_pretty
from utils.pdf_utils import save_resume_pdf
from utils.ats_utils import compute_ats_score

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Apply Wise AI",
    layout="wide"
)

# ---------------- HERO TITLE ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🚀 Apply Wise AI</h1>
    <p style='text-align:center; color:gray;'>
    Analyze job descriptions, match skills, generate resumes & recruiter messages using AI agents
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION STATE INIT ----------------
for key in ["skills", "resume", "message", "ats"]:
    if key not in st.session_state:
        st.session_state[key] = None

# ---------------- LAYOUT ----------------
left_col, right_col = st.columns([1, 1.2])

# ==================================================
# LEFT COLUMN — USER INPUTS
# ==================================================
with left_col:
    st.subheader("👤 Your Details")

    name = st.text_input("Full Name")
    city = st.text_input("City, Country")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    linkedin = st.text_input("LinkedIn URL")
    university = st.text_input("University Name")
    graduation_year = st.text_input("Graduation Year")

    st.subheader("📄 Job Information")
    job_description = st.text_area(
        "Paste Job Description",
        height=160
    )

    recruiter_name = st.text_input("Recruiter Name (optional)")

    st.subheader("🧠 Your Profile")
    candidate_profile = st.text_area(
        "Education, Skills, Projects",
        height=160
    )

    if st.button("🚀 Run AI Agents", use_container_width=True):
        if not job_description or not candidate_profile:
            st.error("Please fill in both Job Description and Profile.")
        else:
            with st.spinner("Running AI agents..."):
                result = run_job_search_ai(job_description, candidate_profile)

                st.session_state.skills = result["skills"].exported_output
                st.session_state.message = result["message"].exported_output

                st.session_state.resume = format_resume_pretty(
                    raw_resume=result["resume"].exported_output,
                    name=name,
                    city=city,
                    phone=phone,
                    email=email,
                    linkedin=linkedin,
                    university=university,
                    graduation_year=graduation_year,
                )

                st.session_state.ats = compute_ats_score(
                    job_description,
                    st.session_state.resume
                )

            st.success("AI agents finished successfully!")

# ==================================================
# RIGHT COLUMN — OUTPUTS
# ==================================================
with right_col:

    if st.session_state.skills:
        st.subheader("🧠 Extracted Skills")
        st.markdown(st.session_state.skills)

    if st.session_state.ats:
        st.subheader("📊 JD Match Score")

        st.metric(
            label="Match Percentage",
            value=f"{st.session_state.ats['score']}%"
        )

        st.markdown("### 🔍 Skill Match Breakdown")

        matched_df = pd.DataFrame({
            "Skill": st.session_state.ats["matched"],
            "Status": ["Matched"] * len(st.session_state.ats["matched"])
        })

        missing_df = pd.DataFrame({
            "Skill": st.session_state.ats["missing"],
            "Status": ["Missing"] * len(st.session_state.ats["missing"])
        })

        skill_table = pd.concat(
            [matched_df, missing_df],
            ignore_index=True
        )

        st.dataframe(
            skill_table,
            use_container_width=True,
            hide_index=True
        )

    if st.session_state.message:
        st.subheader("💬 Recruiter / LinkedIn Message")

        msg = st.session_state.message

        if recruiter_name:
            msg = msg.replace("[Recruiter Name]", recruiter_name)
        else:
            msg = msg.replace("[Recruiter Name]", "Hello")

        msg = msg.replace("[Role Name]", "the role")

        st.markdown(msg)

    if st.session_state.resume:
        st.subheader("📄 Final Resume Preview")
        st.text(st.session_state.resume)

        pdf_path = save_resume_pdf(st.session_state.resume)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Download Resume as PDF",
                data=f,
                file_name="AI_Generated_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
