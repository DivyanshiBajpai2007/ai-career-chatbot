import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🎯",
    layout="wide"
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
SYSTEM_PROMPT = """You are CareerBot, an expert AI career coach for CSE and AI engineering students in India who want to crack top tech companies like Google, Microsoft, Amazon, and Meta.

You were built by Divyanshi Bajpai, a 3rd year CSE-AI student from MPGI Kanpur.

YOUR EXPERTISE:
- Personalized roadmaps based on current skills and target company
- DSA preparation strategy (LeetCode, Codeforces, HackerRank)
- AI/ML skills that actually matter for jobs
- Which certifications are worth it: Azure AI, AWS ML, Google Cloud
- Resume tips for Indian CS students
- LinkedIn and GitHub profile optimization
- Project ideas that stand out in interviews
- How to get internships from tier-2/tier-3 colleges
- System design basics for fresher interviews
- Behavioral interview tips (STAR method)

YOUR STYLE:
- Talk like a helpful senior student, not a textbook
- Be specific, give exact resources and platform names
- Be honest, tell students what actually works
- Be encouraging, many students feel lost
- Keep answers structured with bullet points
- Give PERSONALIZED plans, not generic advice
- Always mention free resources first"""

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a192f 0%, #112240 50%, #0a192f 100%);
    }
    [data-testid="stSidebar"] * {
        color: #ccd6f6 !important;
    }
    [data-testid="stSidebar"] .stButton button {
        background: #112240 !important;
        color: #64ffda !important;
        border: 1px solid #64ffda !important;
        border-radius: 8px !important;
        font-size: 13px !important;
        transition: all 0.3s ease;
    }
    [data-testid="stSidebar"] .stButton button:hover {
        background: #64ffda !important;
        color: #0a192f !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: #1d3557 !important;
    }
    /* Profile section */
    .profile-box {
        background: #112240;
        border: 1px solid #1d3557;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .profile-avatar {
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #64ffda, #0070f3);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.5rem;
        font-size: 24px;
    }
    .profile-name {
        color: #ccd6f6;
        font-weight: 600;
        font-size: 15px;
        margin: 0;
    }
    .profile-title {
        color: #64ffda;
        font-size: 12px;
        margin: 2px 0 0;
    }
    /* Main header */
    .main-header {
        background: linear-gradient(135deg, #0070f3 0%, #0a192f 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1.5rem;
        border: 1px solid #1d3557;
    }
    .main-header h1 {
        margin: 0 0 0.5rem;
        font-size: 2rem;
    }
    .main-header p {
        margin: 0;
        opacity: 0.85;
        font-size: 14px;
    }
    /* Feature cards */
    .feature-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    /* Section label */
    .section-label {
        color: #64ffda !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        margin-bottom: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="profile-box">
        <div class="profile-avatar">👩‍💻</div>
        <p class="profile-name">Divyanshi Bajpai</p>
        <p class="profile-title">3rd Year CSE-AI | MPGI Kanpur</p>
        <p class="profile-title">Aspiring AI Engineer @ Microsoft</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-label">Navigate</p>', unsafe_allow_html=True)
    st.page_link("app.py", label="💬  Chat with CareerBot")
    st.page_link("pages/1_Roadmap_Generator.py", label="🗺️  Roadmap Generator")
    st.page_link("pages/2_Resume_Reviewer.py", label="📄  Resume Reviewer")

    st.divider()
    st.markdown('<p class="section-label">Quick Topics</p>', unsafe_allow_html=True)
    topics = ["Career Roadmap", "DSA Preparation", "AI/ML Skills", "Resume Tips", "Interview Prep", "Project Ideas"]
    for topic in topics:
        if st.button(topic, use_container_width=True, key=topic):
            question = "Give me advice on: " + topic
            st.session_state.messages.append({"role": "user", "content": question})
            st.rerun()

    st.divider()
    st.markdown('<p class="section-label">Connect</p>', unsafe_allow_html=True)
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com)")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com)")
    st.divider()
    if st.button("🗑️  Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown("""
<div class="main-header">
    <h1>🎯 AI Career Coach</h1>
    <p>Your personal guide to cracking Google, Microsoft & top tech companies</p>
    <p>Built for CSE-AI students in India &nbsp;|&nbsp; Powered by Llama 3.3 70B</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.info("🗺️ **Roadmap Generator**\nGet a personalized month-by-month career plan")
with col2:
    st.success("📄 **Resume Reviewer**\nGet detailed AI feedback on your resume")
with col3:
    st.warning("💬 **Career Chatbot**\nAsk anything about your tech career")

st.divider()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if len(st.session_state.messages) == 0:
    st.markdown("### 👋 Hi! What do you want to work on today?")
    col1, col2 = st.columns(2)
    suggestions = [
        "Make me a 3-month roadmap for Google",
        "What AI skills do I need for Microsoft?",
        "How should my resume look as a fresher?",
        "Suggest projects that impress recruiters",
        "How do I start DSA from scratch?",
        "Which certifications are worth doing?",
    ]
    for i, suggestion in enumerate(suggestions):
        if i % 2 == 0:
            if col1.button(suggestion, use_container_width=True, key=suggestion):
                st.session_state.messages.append({"role": "user", "content": suggestion})
                st.rerun()
        else:
            if col2.button(suggestion, use_container_width=True, key=suggestion):
                st.session_state.messages.append({"role": "user", "content": suggestion})
                st.rerun()

if prompt := st.chat_input("Ask me anything about your tech career..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                max_tokens=1024
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
