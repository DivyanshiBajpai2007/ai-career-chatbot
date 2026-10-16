# AI Career Coach

Multi-page Streamlit app giving career guidance to CSE/AI students in India: a chatbot, a roadmap generator and a resume reviewer. Deployed on Streamlit Cloud (see README for the live link).

## Layout
- `app.py`: main chatbot page (keeps chat history in `st.session_state`)
- `pages/1_Roadmap_Generator.py`: form → month-by-month roadmap (downloadable)
- `pages/2_Resume_Reviewer.py`: pasted resume → score, gaps, ATS keywords, top fixes (downloadable)
- `create_final_app.py`, `create_page.py`, `create_resume_page.py`: old generator scripts, not part of the running app

## Stack
- Python, Streamlit, Groq API with `openai/gpt-oss-120b` (migrated from the retired `llama-3.3-70b-versatile`). `anthropic` is also listed in requirements.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
Secrets: `GROQ_API_KEY` in `.streamlit/secrets.toml` (git-ignored, never commit it or print it).

## Conventions
- `MODEL` is currently defined separately in `app.py` and in each page. When migrating models, update all three, or move the name into a shared `config.py`.
- Pages are independent Streamlit scripts. Shared logic should go in a helper module rather than being copy-pasted.
- Keep it deployable on Streamlit Cloud (light dependencies).
- Commits: no Claude co-author or "Generated with Claude Code" lines.
