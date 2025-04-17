import streamlit as st
import os
import warnings
from agents.scraper import scrape_article_text
from agents.pdf_scraper import extract_text_from_pdf
from llm.gemma_runner import generate_summary_with_gemma
from agents.formatter import format_summary
from agents.example_generator import generate_examples_with_gemma
from agents.compiler import compile_to_markdown, convert_markdown_to_pdf
from rag.qna_rag import chunk_text, build_faiss_index, retrieve_context, ask_question
from voice.voice_input import record_and_transcribe  # 🎤 Voice input

warnings.filterwarnings("ignore", category=UserWarning)
st.set_page_config(page_title="LearnWeaver", page_icon="🧠", layout="centered")

st.title("🧠 LearnWeaver — AI Textbook & Notes Generator")
st.markdown("Upload up to **4 inputs**: PDF files and article/newsletter links. I’ll combine them into a single textbook 📘 or notebook 📝 with examples and a Q&A tutor.")

# ---- Session State ----
if "raw_text" not in st.session_state:
    st.session_state.raw_text = ""
if "qna_ready" not in st.session_state:
    st.session_state.qna_ready = False
    st.session_state.qa_chunks = None
    st.session_state.qa_index = None
    st.session_state.qa_embeddings = None
    st.session_state.qa_text = None

raw_parts = []

# ---- Article Links ----
st.markdown("### 🔗 Article / Newsletter Links (up to 3)")
for i in range(1, 4):
    link = st.text_input(f"Link {i}")
    if link:
        with st.spinner(f"Scraping Link {i}..."):
            try:
                text = scrape_article_text(link)
                raw_parts.append(text)
                st.success(f"✅ Link {i} content extracted.")
            except Exception as e:
                st.error(f"❌ Failed to scrape Link {i}: {e}")

# ---- PDF Uploads ----
st.markdown("### 📄 Upload PDFs (You can upload multiple)")
pdf_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
if pdf_files:
    for idx, pdf in enumerate(pdf_files):
        with st.spinner(f"Extracting PDF {idx + 1}..."):
            with open(f"temp_{idx}.pdf", "wb") as f:
                f.write(pdf.read())
            text = extract_text_from_pdf(f"temp_{idx}.pdf")
            raw_parts.append(text)
    st.success("✅ All PDFs processed.")

# ---- Combine Inputs ----
if raw_parts:
    st.session_state.raw_text = "\n\n".join(raw_parts)

# ---- Preview Input ----
if st.session_state.raw_text:
    st.markdown("## 📄 Combined Content Preview")
    st.info(f"📏 Total Characters: {len(st.session_state.raw_text)}")
    st.text_area("📝 Preview:", value=st.session_state.raw_text[:3000], height=200)

# ---- Output Generation ----
if st.session_state.raw_text:
    st.markdown("### ✨ Generate Learning Material")
    grade = st.selectbox("Target Grade Level", ["Grade 2", "Grade 6", "High School", "Undergrad", "Masters", "PhD"])
    style = st.radio("Choose Format", ["Textbook", "Notebook"])

    if st.button("🧠 Generate Content"):
        with st.spinner("🔎 Summarizing with Gemma..."):
            summary = generate_summary_with_gemma(st.session_state.raw_text, grade_level=grade, output_format=style.lower())

        with st.spinner("🧪 Creating Examples..."):
            examples = generate_examples_with_gemma(summary, grade_level=grade)

        with st.spinner("🖋️ Formatting Output..."):
            formatted = format_summary(summary, output_format=style.lower(), grade_level=grade)

        with st.spinner("📄 Compiling to PDF..."):
            os.makedirs("output/markdown", exist_ok=True)
            os.makedirs("output/pdf", exist_ok=True)
            md_path = compile_to_markdown(formatted, examples, output_format=style.lower(), filename="learnweaver_output")
            pdf_path = convert_markdown_to_pdf(md_path)

        st.success("🎉 Learning Material Generated!")

        # ---- Preview Output ----
        st.markdown("## 🧾 Final Output Preview")
        st.text_area("📘 Content", value=formatted + "\n\n" + examples, height=400)

        # ---- Download PDF ----
        st.download_button("📥 Download PDF", data=open(pdf_path, "rb"), file_name="LearnWeaver_Output.pdf")

        # ---- Setup Q&A State ----
        with st.spinner("🔗 Setting up Agentic Q&A..."):
            combined_text = formatted + "\n\n" + examples
            chunks = chunk_text(combined_text)
            index, embeddings, stored_chunks = build_faiss_index(chunks)
            st.session_state.qa_chunks = stored_chunks
            st.session_state.qa_index = index
            st.session_state.qa_embeddings = embeddings
            st.session_state.qna_ready = True
            st.session_state.qa_text = combined_text

# ---- Agentic Q&A Section ----
if st.session_state.qna_ready:
    st.markdown("## 🧑‍🏫 Ask a Question About This Topic")

    col1, col2 = st.columns([3, 1])
    with col1:
        user_question = st.text_input("💬 Type your question:")
    with col2:
        if st.button("🎙️ Voice"):
            with st.spinner("🎤 Listening..."):
                user_question = record_and_transcribe()
                if user_question:
                    st.info(f"🗣️ You said: {user_question}")
                else:
                    st.warning("❗ Voice input was not recognized.")

    if user_question:
        with st.spinner("🤖 Thinking..."):
            context = retrieve_context(user_question, st.session_state.qa_index, st.session_state.qa_chunks, st.session_state.qa_embeddings)
            answer = ask_question(user_question, context)
        st.markdown("### 📘 Answer")
        st.success(answer)
