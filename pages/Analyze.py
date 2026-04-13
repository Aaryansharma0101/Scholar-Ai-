import streamlit as st
from Backend.Analyzer import process_pdf, generate_summary, ask_question
from Backend.Similarity import add_paper, find_similar
from Backend.Similarity import add_paper, find_similar

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

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
        if st.button("Home", key="home_analyze"):
            st.switch_page("app.py")

    with c2:
        if st.button("Analyze", key="analyze_analyze"):
            st.switch_page("pages/Analyze.py")

    with c3:
        if st.button("Compare", key="compare_analyze"):
            st.switch_page("pages/Compare.py")

st.markdown("<hr>", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown(
    "<h1 style='color:white;'>Analyze Research Paper</h1>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---- FILE UPLOADER (NEW) ----
uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"],
    key="analyze_upload"
)

st.markdown("<br>", unsafe_allow_html=True)

# ---- MAIN LAYOUT ----
col_left, col_right = st.columns([1, 1.2])

with col_left:
    if uploaded_file:
        st.markdown(
            f"<div style='background:#111827;padding:25px;border-radius:16px;color:white;'>"
            f"📄 {uploaded_file.name}"
            f"<br><br>PDF Preview Area (we can render later)"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background:#111827;padding:25px;border-radius:16px;color:#A0AEC0;'>"
            "Upload a PDF to preview it here."
            "</div>",
            unsafe_allow_html=True
        )

with col_right:
    tabs = st.tabs(["Summary", "Ask AI", "Key Insights", "Related Papers"])

    if uploaded_file:

        # 🔥 Load backend once
        from Backend.Analyzer import process_pdf, generate_summary, ask_question

        if "data" not in st.session_state:
            with st.spinner("Processing paper..."):
                st.session_state.data = process_pdf(uploaded_file)

        data = st.session_state.data

        add_paper(data["text"])
    # ===================== SUMMARY =====================

    with tabs[0]:

        if uploaded_file:

            if st.button("Generate Summary"):

                with st.spinner("Generating summary..."):
                    summary = generate_summary(data["text"], data["summarizer"])

                st.markdown(
                    f"<div style='background:#111827;padding:20px;border-radius:12px;color:white;'>{summary}</div>",
                    unsafe_allow_html=True
                )

        else:
            st.write("Upload a file to generate summary.")

    # ===================== ASK AI =====================

    with tabs[1]:

        if uploaded_file:

            question = st.text_input("Ask a question about the paper")

            if st.button("Ask AI") and question:

                with st.spinner("Thinking..."):
                    answer = ask_question(question, data["rag"])

                st.markdown(
                    f"<div style='background:#111827;padding:20px;border-radius:12px;color:white;'>{answer}</div>",
                    unsafe_allow_html=True
                )

        else:
            st.write("Upload a file first.")

    # ===================== KEY INSIGHTS =====================

    with tabs[2]:

        if uploaded_file:

            if st.button("Extract Key Insights"):

                with st.spinner("Extracting insights..."):

                    prompt = f"""
Extract the key insights from this research paper.

Include:
- main contribution
- important findings
- key takeaways

Write in bullet points.

Paper:
{data["text"][:3000]}
"""

                    insights = data["summarizer"].llm.generate(prompt)

                st.markdown(
                    f"<div style='background:#111827;padding:20px;border-radius:12px;color:white;'>{insights}</div>",
                    unsafe_allow_html=True
                )

        else:
            st.write("Upload a file first.")

    # ===================== RELATED PAPERS =====================

    with tabs[3]:

        if uploaded_file:

            if st.button("Find Related Papers"):

                with st.spinner("Finding similar research..."):

                    results = find_similar(data["text"])

                    st.markdown("###  Related Papers")

                    for i, r in enumerate(results):
                        st.markdown(
                            f"""
                            <div style='
                                background:#111827;
                                padding:15px;
                                border-radius:10px;
                                color:white;
                                margin-bottom:10px;
                            '>
                            <b>Paper {i+1}</b><br>
                            {r[:300]}...
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

        else:
            st.write("Upload a paper first.")