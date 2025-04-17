# AI-Learn-Weaver


# 🧠 LearnWeaver — AI-Powered Textbook & Notes Generator

LearnWeaver is an intelligent education assistant that generates structured learning material from PDFs and article/newsletter links. It produces textbook-style or notebook-style content, complete with examples and an interactive Q&A tutor mode — all powered by local LLMs and retrieval-based techniques.

---

## 🚀 Features

✅ Upload **multiple PDFs** and **article/newsletter links**  
✅ Automatically extract and summarize raw educational content using **Gemma via Ollama**  
✅ Generate **examples, exercises, and real-world problems**  
✅ Format output in **Textbook** or **Notebook** style  
✅ Export final content as **PDF**  
✅ Built-in **Q&A Tutor Mode** using FAISS + local Gemma  
✅ 🎤 Voice-based question input using **Whisper**  
✅ No external API required — runs **fully local** with Ollama

---

## 🧪 Technologies Used

| Component          | Technology / Library               |
|--------------------|------------------------------------|
| LLM                | [Gemma 7B](https://ollama.com/library/gemma) via Ollama |
| Embeddings         | Sentence-Transformers              |
| Vector DB          | FAISS                              |
| Voice Input        | Whisper + SpeechRecognition        |
| PDF Parsing        | PyMuPDF                            |
| Web Scraping       | newspaper3k + yt_dlp               |
| Frontend           | Streamlit                          |
| Output Format      | Markdown + PDF                     |
| Q&A Search         | Retrieval-Augmented Generation (RAG) |
| Deployment (Demo)  | Streamlit Cloud                    |

---

## 📸 Screenshots

> ✅ Upload PDFs and Links  
> ✅ Get textbook output with examples  
> ✅ Ask questions via text or mic  
> ✅ Download final PDF

Checkout the app: https://ai-learn-weaver-gzzmlx7xeloq327qldqtha.streamlit.app/

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

# Install dependencies
pip install -r requirements.txt

# Make sure Ollama + Gemma is installed
ollama run gemma:7b
LearnWeaver/
│
├── interface/            # Streamlit UI
├── agents/               # Scrapers, compilers, formatter
├── llm/                  # Gemma runners
├── rag/                  # Q&A RAG pipeline
├── voice/                # Whisper input handler
├── output/               # Generated markdown + PDFs
├── tools/                # Tool wrappers (LLM tools for CrewAI - WIP)
├── crew/                 # CrewAI config & agents (WIP)
├── requirements.txt
└── README.md
🔮 Coming Soon
✅ CrewAI Agent Orchestration

Multi-agent pipeline to handle summarization, example generation, formatting using CrewAI

Fully modular, pluggable tool-based workflows

✅ Mobile App (React Native)

Seamless mobile deployment with voice-driven question answering

Save, share, and bookmark custom textbooks
