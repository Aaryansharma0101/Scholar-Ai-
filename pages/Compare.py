import streamlit as st
from models.llm_model import LLMModel
import fitz  # PyMuPDF
import tempfile

st.set_page_config(layout="wide")

# ---- Hide Sidebar + Dark Theme ----
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
footer {visibility: hidden;}
body {background-color:#0B0F19;}

div.stButton > button:hover {
    box-shadow: 0px 0px 20px rgba(79,140,255,0.5);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
col1, col2 = st.columns([6,2])

with col1:
    st.markdown("<h2 style='color:white;'>ScholarAI</h2>", unsafe_allow_html=True)

with col2:
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("Home"):
            st.switch_page("app.py")

    with c2:
        if st.button("Analyze"):
            st.switch_page("pages/Analyze.py")

    with c3:
        if st.button("Compare"):
            st.switch_page("pages/Compare.py")

st.markdown("<hr>", unsafe_allow_html=True)

# ---- TITLE ----
st.title("Test Your Research Papers")

# ---- LOAD MODEL ----
@st.cache_resource
def load_llm():
    return LLMModel()

llm = load_llm()

# ------------------ FILE UPLOAD ------------------
uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type=["pdf"]
)

# ------------------ BUTTONS (ALWAYS VISIBLE) ------------------
st.markdown("### Analyze Your Paper")

col1, col2, col3, col4 = st.columns(4)

with col1:
    gap_btn = st.button("Research Gaps", use_container_width=True)

with col2:
    method_btn = st.button("Method Breakdown", use_container_width=True)

with col3:
    limit_btn = st.button("Limitations", use_container_width=True)

with col4:
    improve_btn = st.button("Improvement Suggestions", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------ PROCESS LOGIC ------------------
if uploaded_file:

    # 🔥 Save PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # 🔥 Extract text using PyMuPDF
    doc = fitz.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text("text")

    text = text[:3000]  # limit for speed

    st.success("✅ Paper loaded successfully!")

    # -------- RESEARCH GAPS --------
    if gap_btn:
        with st.spinner("Finding research gaps..."):
            prompt = f"""
You are a research expert.

Identify research gaps in this paper.
Give clear bullet points.

Paper:
{text}
"""
            result = llm.generate(prompt)
            st.subheader("Research Gaps")
            st.write(result)

    # -------- METHOD BREAKDOWN --------
    if method_btn:
        with st.spinner("Analyzing methodology..."):
            prompt = f"""
Explain the methodology used in this paper in simple terms.

Paper:
{text}
"""
            result = llm.generate(prompt)
            st.subheader("Method Breakdown")
            st.write(result)

    # -------- LIMITATIONS --------
    if limit_btn:
        with st.spinner("Analyzing limitations..."):
            prompt = f"""
What are the limitations of this research paper?
Give concise bullet points.

Paper:
{text}
"""
            result = llm.generate(prompt)
            st.subheader("⚠️ Limitations")
            st.write(result)

    # -------- IMPROVEMENTS --------
    if improve_btn:
        with st.spinner("Generating improvements..."):
            prompt = f"""
Suggest improvements or future enhancements for this paper.

Paper:
{text}
"""
            result = llm.generate(prompt)
            st.subheader("Improvements")
            st.write(result)

# ------------------ NO FILE CASE ------------------
else:
    if gap_btn or method_btn or limit_btn or improve_btn:
        st.warning("⚠️ Please upload a research paper first.")
    else:
        st.info("Upload a paper to start deep analysis.")
