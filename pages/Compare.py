# ------------------ PROCESS LOGIC ------------------
if uploaded_file:

    import fitz  # PyMuPDF
    import tempfile

    # 🔥 Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # 🔥 Extract text properly
    doc = fitz.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text()

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
