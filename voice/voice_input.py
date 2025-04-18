import os
import speech_recognition as sr

def record_and_transcribe():
    # Detect if we're running in Streamlit Cloud or headless environment
    if os.environ.get("STREAMLIT_SERVER_HEADLESS", "0") == "1":
        return "🎙️ Voice input not available in cloud environment."

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            audio = recognizer.listen(source)
            print("🧠 Transcribing...")

        return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        return "❗ Sorry, I couldn't understand your voice."
    except sr.RequestError as e:
        return f"❗ API request failed: {e}"
    except Exception as e:
        return f"🎤 Voice input not working: {e}"
