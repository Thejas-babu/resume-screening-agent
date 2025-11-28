import streamlit as st
import pandas as pd

from agent import screen_resume
from resume_parser import parse_resume
from ranking import rank_candidates

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)

# -------------------- DARK THEME CSS --------------------
st.markdown("""
<style>
* { font-family: "JetBrains Mono", monospace; }

body {
    background: radial-gradient(circle at top left, #020617, #030712);
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(148,163,184,0.4);
    backdrop-filter: blur(18px);
    box-shadow: 0px 14px 35px rgba(0,0,0,0.7);
    margin-bottom: 22px;
}

/* JD Hover Card */
.jd-card {
    background: linear-gradient(145deg, rgba(15,23,42,0.98), rgba(30,64,175,0.7));
    border: 1px solid rgba(56,189,248,0.55);
    transition: all 0.18s ease-out;
}
.jd-card:hover {
    border-color: #38bdf8;
    box-shadow: 0px 20px 50px rgba(0,187,255,0.4);
    transform: translateY(-3px);
}

/* Header */
h1 {
    color: #00E1FF;
    text-align: center;
    font-weight: 800;
}
.section-header {
    color: #f8fafc;
    font-size: 19px;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    padding: 12px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 18px;
    color: white;
    background: linear-gradient(135deg, #00e1ff, #305EFF);
    border: 0;
    transition: 0.22s;
}
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 15px 30px rgba(0,181,255,0.35);
}

/* Table */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown(
        """
        <div style="padding:16px; border-radius:12px; 
        background:rgba(15,23,42,0.9);
        border:1px solid rgba(148,163,184,0.5); 
        backdrop-filter:blur(12px);">
        
        <h3 style="color:#00E1FF; margin-bottom:10px;">ℹ About This App</h3>
        <p style="color:#dce2ed; font-size:13px; line-height:1.6;">
        This AI Resume Screening tool uses the Llama3 model via the Groq API to evaluate candidate resumes against a provided job description. 
        It assigns a score, detects strengths/weaknesses, and ranks all candidates based on job fit.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("""
    **🧠 Powered By:**
    - Groq Llama 3
    - Streamlit UI
    - Python + Pandas
    - PDF/DOCX Extractor
    """)

    st.markdown("---")

    st.caption("📌 Version 1.0 — Built by Thejas Babu")

# -------------------- HEADER --------------------
st.markdown("<h1>📄 AI Resume Screening Agent</h1>", unsafe_allow_html=True)
st.write("### Upload resumes + job description → Get ranked insights")

# -------------------- UI LAYOUT --------------------
col1, col2 = st.columns([1.4, 1])

# ---- LEFT: Job Description ----
with col1:
    st.markdown('<div class="card jd-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🧾 Job Description</div>', unsafe_allow_html=True)
    jd_text = st.text_area(
        "Paste Job Description here:",
        height=260,
        placeholder="Example: Required skills, tools, years of experience, responsibilities..."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---- RIGHT: Upload Section ----
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">📁 Upload Resumes</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "Upload one or more resumes (.pdf/.docx)",
        accept_multiple_files=True,
        type=["pdf","docx"]
    )
    st.markdown("<small style='opacity:0.75;'>Tip: Rename files by candidate name for cleaner ranking.</small>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---- ACTION BUTTON ----
run = st.button("🚀 Run Screening", use_container_width=True)

# -------------------- PROCESSING --------------------
if run:
    if not jd_text:
        st.error("⚠ Please paste a job description first.")
    elif not uploaded_files:
        st.error("⚠ Please upload at least one resume.")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">⏳ Screening Progress</div>', unsafe_allow_html=True)

        progress = st.progress(0)
        status = st.empty()
        results = []

        for i, file in enumerate(uploaded_files):
            status.write(f"📄 Processing: **{file.name}**")
            resume_text = parse_resume(file)
            analysis = screen_resume(resume_text, jd_text)

            results.append({
                "Candidate": file.name,
                "score": analysis.get("score", 0),
                "Fit %": analysis.get("fit_percentage", 0),
                "Decision": analysis.get("decision", "N/A"),
                "Strengths": ", ".join(analysis.get("strengths", [])),
                "Weaknesses": ", ".join(analysis.get("weaknesses", [])),
                "Reasoning": analysis.get("reasoning", ""),
            })

            progress.progress((i+1) / len(uploaded_files))

        st.markdown("</div>", unsafe_allow_html=True)

        df = rank_candidates(results)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🏆 Ranked Candidates</div>', unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False)
        st.download_button(
            "⬇ Download CSV Results",
            csv,
            "screening_results.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="card">
    <div class="section-header">🚀 How to use</div>
    <ul style='color:#cbd5e1; font-size:14px; line-height:1.6;'>
        <li>Paste the job description on the left.</li>
        <li>Upload candidate resumes (PDF/DOCX) on the right.</li>
        <li>Click <b>Run Screening</b> to evaluate and rank the resumes.</li>
        <li>Download CSV results for further review.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
