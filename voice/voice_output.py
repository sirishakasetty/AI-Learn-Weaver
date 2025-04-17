import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Adjust speaking speed if needed
    engine.say(text)
    engine.runAndWait()
