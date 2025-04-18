import os
import speech_recognition as sr

def record_and_transcribe():
    """
    Records voice input using a microphone and transcribes it to text using Google's speech recognition API.
    If running in Streamlit Cloud (headless), it returns a message stating voice is unavailable.
    """

    # Disable mic in Streamlit Cloud or headless environments
    if os.environ.get("STREAMLIT_SERVER_HEADLESS", "0") == "1":
        return "🎙️ Voice input is not supported in Streamlit Cloud. Please type your question."

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("🧠 Transcribing...")
            return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        return "❗ Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"❗ API request error: {e}"
    except Exception as e:
        return f"🎤 Voice input error: {str(e)}"
