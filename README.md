# 🧠 LearnWeaver – AI Textbook & Notes Generator

LearnWeaver is an AI-powered Streamlit app that transforms PDFs, article links, or newsletters into structured educational content. It generates chapter-style summaries, practical examples, and includes a Q&A tutor mode — tailored for learners from Grade 2 to PhD.

---

## 🚀 Features

- 📄 **Upload PDFs or Enter Article Links**  
- 🧠 **Generate Textbook or Notebook-Style Summaries**  
- 🧪 **Real-World and Exam-Style Examples**  
- 🗣️ **Voice Input Support for Q&A**  
- ❓ **Ask Questions with Agentic Retrieval**  
- 📥 **Download as PDF**  

---

## 🧰 Tech Stack

| Component      | Technology                         |
|----------------|------------------------------------|
| LLM            | OpenAI GPT-3.5 Turbo (API)         |
| Interface      | Streamlit                          |
| Voice Input    | Whisper, Pyttsx3                   |
| Document Parsing | PyMuPDF, newspaper3k             |
| Vector DB      | FAISS + Sentence Transformers      |
| Output         | Markdown, PDF (FPDF, markdown2)    |

---

## ⚙️ Setup Instructions

### 1. Clone this repo:
```bash
git clone https://github.com/sirishakasetty/AI-Learn-Weaver.git
cd AI-Learn-Weaver

---

## 📸 Screenshots

> ✅ Upload PDFs and Links  
> ✅ Get textbook output with examples  
> ✅ Ask questions via text or mic  
> ✅ Download final PDF

Checkout the app:(https://ai-learn-weaver-gzzmlx7xeloq327qldqtha.streamlit.app/)

---

## 🧑‍🏫 How to Use

1. Clone the repository  
2. Set up the environment (instructions below)  
3. Launch the app with `streamlit run interface/app_ui.py`  
4. Upload your files, choose format, and explore the Q&A features

---

## 📦 Installation

```bash
# Create and activate environment (e.g. with conda)
conda create -n learnweaver python=3.10
conda activate learnweaver

🔑 OpenAI Key Setup
Get your key from https://platform.openai.com/account/api-keys

Create a .streamlit/secrets.toml file:
OPENAI_API_KEY = "your-openai-key"



# Install dependencies
pip install -r requirements.txt

📦 Folder Structure
LearnWeaver/
│
├── interface/
│   └── app_ui.py
│
├── agents/
│   ├── scraper.py
│   ├── pdf_scraper.py
│   ├── example_generator.py
│   ├── formatter.py
│   └── compiler.py
│
├── llm/
│   └── gemma_runner.py  <-- (Now uses OpenAI)
│
├── rag/
│   └── qna_rag.py
│
├── voice/
│   └── voice_input.py
│
└── output/
    ├── markdown/
    └── pdf/

🔮 Coming Soon
🏁 Future Roadmap
✅ Add OpenAI fallback if Ollama not available

🔁 Integrate CrewAI agents

📱 Launch mobile version via React Native

📊 Feedback logging and dashboard

