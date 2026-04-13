import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# ===================== GLOBAL STYLING =====================

st.markdown("""
<style>

/* Hide sidebar + footer */
section[data-testid="stSidebar"] {display: none;}
footer {visibility: hidden;}

/* ===================== BACKGROUND ===================== */

.stApp {
    background: linear-gradient(160deg, #020617 0%, #697e96 45%, #507daf 100%) !important;
    background-attachment: fixed !important;
}

/* ===================== HERO BUTTONS ===================== */

.hero-buttons div.stButton > button {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    color: white;
    border-radius: 12px;
    padding: 14px 26px;
    border: none;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
}

.hero-buttons div.stButton > button:hover {
    box-shadow: 0px 0px 25px rgba(99,102,241,0.5);
    transform: translateY(-3px);
}

/* Header button hover glow */
div.stButton > button:hover {
    box-shadow: 0px 0px 15px rgba(79,140,255,0.4);
}

</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================

col1, col2 = st.columns([6,2])

with col1:
    st.markdown("<h2 style='color:white;'>ScholarAI</h2>", unsafe_allow_html=True)

with col2:
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("Home", key="home_top"):
            st.switch_page("app.py")

    with c2:
        if st.button("Analyze", key="analyze_top"):
            st.switch_page("pages/Analyze.py")

    with c3:
        if st.button("Compare", key="compare_top"):
            st.switch_page("pages/Compare.py")

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

# ===================== HERO SECTION =====================

col_left, col_right = st.columns([1.1, 1])

with col_left:

    # Badge
    st.markdown("""
    <div style="
        display:inline-block;
        padding:8px 14px;
        background:#092d8c;
        border-radius: 20px;
        color: #FFFFFF;
        font-size:14px;
        margin-bottom:20px;">
        AI-Powered Research Analysis
    </div>
    """, unsafe_allow_html=True)

    # Main Heading
    st.markdown("""
    <h1 style="
        font-size:72px;
        font-weight:700;
        color:#e5e7eb;
        line-height:1.1;
        margin-bottom:30px;">
        Understand papers faster. Extract insights that matter.
    </h1>
    """, unsafe_allow_html=True)

    # Subtext
    st.markdown("""
    <p style="
        font-size:20px;
        color:#FFFFFF;
        max-width:520px;
        margin-bottom:40px;">
        Upload any research paper and get a structured brief in seconds.
        Built for researchers who need clarity, not clutter.
    </p>
    """, unsafe_allow_html=True)

    # Action Buttons
    st.markdown("<div class='hero-buttons'>", unsafe_allow_html=True)

    colA, colB = st.columns([1,1])

    with colA:
        if st.button("Analyze Paper →", key="hero_analyze"):
            st.switch_page("pages/Analyze.py")

    with colB:
        if st.button("Compare Papers →", key="hero_compare"):
            st.switch_page("pages/Compare.py")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Bottom Text
    st.markdown("""
    <p style="color:#9ca3af; font-size:14px;">
        Join thousands of researchers who use ScholarAI to accelerate their literature review.
    </p>
    """, unsafe_allow_html=True)


with col_right:
    st.markdown("""
    <div style="
        background: rgba(0, 0, 0, 0);
        border: 0px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 20px;">
    """, unsafe_allow_html=True)

    st.image("hero.png", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)