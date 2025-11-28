import streamlit as st
import pandas as pd
from resume_parser import parse_resume
from agent import screen_resume
from ranking import rank_candidates

st.title("📄 AI Resume Screening Agent (Gemini — FREE API)")

jd_text = st.text_area("Paste Job Description", height=160)

uploaded_files = st.file_uploader("Upload resumes (PDF/DOCX)", type=["pdf","docx"], accept_multiple_files=True)

if st.button("Run Screening"):
    if not jd_text:
        st.error("❌ Please enter a Job Description.")
        st.stop()

    if not uploaded_files:
        st.error("❌ Please upload resumes.")
        st.stop()

    results = []

    for file in uploaded_files:
        st.write(f"Processing: **{file.name}**")
        resume_text = parse_resume(file)
        result = screen_resume(resume_text, jd_text)

        results.append({
            "name": file.name,
            "score": result.get("score", 0),
            "fit_percentage": result.get("fit_percentage", 0),
            "decision": result.get("decision", "N/A"),
            "strengths": ", ".join(result.get("strengths", [])),
            "weaknesses": ", ".join(result.get("weaknesses", [])),
            "reasoning": result.get("reasoning", "")
        })

    df = rank_candidates(results)
    st.subheader("📊 Ranked Candidates")
    st.dataframe(df)

    st.download_button("Download CSV", df.to_csv(index=False), "results.csv")
