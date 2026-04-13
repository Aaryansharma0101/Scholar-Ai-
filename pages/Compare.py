import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ---- Hide Sidebar + Dark Background ----
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
        if st.button("Home", key="home_compare"):
            st.switch_page("app.py")

    with c2:
        if st.button("Analyze", key="analyze_compare"):
            st.switch_page("pages/Analyze.py")

    with c3:
        if st.button("Compare", key="compare_compare"):
            st.switch_page("pages/Compare.py")

st.markdown("<hr>", unsafe_allow_html=True)

# ---- PAGE TITLE ----
st.markdown(
    "<h1 style='color:white;'>Compare Research Papers</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#A0AEC0;'>Upload 2 or more papers for AI comparison.</p>",
    unsafe_allow_html=True
)

# ---- FILE UPLOADER ----
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True,
    key="compare_uploader"
)

# ---- COMPARE ACTION ----
if uploaded_files:
    if st.button("Compare Now", key="compare_now_btn"):
        st.success("Comparison started...")

        st.markdown(
            "<div style='background:#111827;padding:25px;border-radius:16px;color:white;margin-top:20px;'>"
            "<h3>Related Paper Suggestions</h3>"
            "<ul>"
            "<li>BERT: Pre-training of Deep Bidirectional Transformers</li>"
            "<li>GPT: Improving Language Understanding</li>"
            "<li>Transformer-XL</li>"
            "</ul>"
            "</div>",
            unsafe_allow_html=True
        )