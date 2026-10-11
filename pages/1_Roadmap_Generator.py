import streamlit as st
from groq import Groq

st.set_page_config(page_title="Roadmap Generator", layout="wide")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL = "openai/gpt-oss-120b"

st.title("Roadmap Generator")
st.caption("Fill in your details and get a custom career roadmap")
st.divider()

with st.form("roadmap_form"):
    name = st.text_input("Your Name")
    target_company = st.selectbox("Target Company", ["Google", "Microsoft", "Amazon", "Meta"])
    target_role = st.selectbox("Target Role", ["AI Engineer", "Software Engineer", "Data Scientist"])
    time_available = st.selectbox("Time Available", ["1 month", "3 months", "6 months", "1 year"])
    current_skills = st.text_area("Your Current Skills")
    goal = st.text_area("Any specific goal?")
    submitted = st.form_submit_button("Generate My Roadmap", use_container_width=True)

if submitted:
    prompt = f"Create a detailed career roadmap for {name}, targeting {target_role} at {target_company}. Time: {time_available}. Skills: {current_skills}. Goal: {goal}. Give month by month plan with free resources and project ideas."
    with st.spinner("Generating your roadmap..."):
        response = client.chat.completions.create(
            model=MODEL,
            reasoning_effort="low",
            messages=[
                {"role": "system", "content": "You are an expert career coach for CSE/AI students in India."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4096
        )
        roadmap = response.choices[0].message.content
    st.success("Your roadmap is ready!")
    st.markdown(roadmap)
    st.download_button("Download My Roadmap", data=roadmap, file_name="roadmap.txt", mime="text/plain", use_container_width=True)
