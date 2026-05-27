import streamlit as st
from groq import Groq

st.set_page_config(page_title="Resume Reviewer", layout="wide")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("Resume Reviewer")
st.caption("Paste your resume and get detailed AI feedback for your target company")
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    resume_text = st.text_area("Paste your resume text here", height=400, placeholder="Paste your full resume text here...")

with col2:
    st.markdown("### Settings")
    target_company = st.selectbox("Target Company", ["Google", "Microsoft", "Amazon", "Meta", "Any Top MNC"])
    target_role = st.selectbox("Target Role", ["AI Engineer", "Software Engineer", "Data Scientist", "ML Engineer"])
    year = st.selectbox("Your Year", ["1st Year", "2nd Year", "3rd Year", "4th Year", "Fresher"])
    st.divider()
    st.markdown("**What you will get:**")
    st.markdown("- Overall resume score out of 10")
    st.markdown("- Missing skills for your target role")
    st.markdown("- Weak sections to improve")
    st.markdown("- Projects feedback")
    st.markdown("- Keywords to add for ATS systems")

st.divider()

if st.button("Review My Resume", use_container_width=True, type="primary"):
    if not resume_text or len(resume_text) < 50:
        st.warning("Please paste your resume text first!")
    else:
        prompt = "You are an expert resume reviewer. Review this resume for a " + year + " CSE/AI student targeting " + target_role + " at " + target_company + ". Resume: " + resume_text + " Give a detailed review with these sections: 1. OVERALL SCORE out of 10. 2. STRENGTHS: 3-5 good points. 3. MISSING SKILLS for this role. 4. WEAK SECTIONS and how to fix them. 5. PROJECTS FEEDBACK and what projects to add. 6. ATS KEYWORDS: 10 keywords to add. 7. TOP 3 URGENT FIXES. Be specific, honest and encouraging."

        with st.spinner("Reviewing your resume..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are an expert resume reviewer and career coach for CSE/AI students in India targeting top tech companies. Be specific, honest and helpful."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2048
            )
            review = response.choices[0].message.content

        st.success("Resume review complete!")
        st.divider()
        st.markdown(review)
        st.divider()
        st.download_button(
            "Download My Resume Review",
            data=review,
            file_name="resume_review.txt",
            mime="text/plain",
            use_container_width=True
        )
