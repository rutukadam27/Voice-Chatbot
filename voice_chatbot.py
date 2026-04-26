import speech_recognition as sr
import pyttsx3

# voice engine
engine = pyttsx3.init()

# function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function to listen voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        return ""

# chatbot logic
def chatbot_reply(text):
    if "hello" in text or "hi" in text:
        return "Hello, how can I help you?"
    elif "name" in text:
        return "I am a voice chatbot made using Python"
    elif "bye" in text:
        return "Goodbye, have a nice day"
    else:
        return "Sorry, I did not understand"

# main program
speak("Voice chatbot started")

while True:
    user_text = listen()
    reply = chatbot_reply(user_text)
    print("Bot:", reply)
    speak(reply)

    if "bye" in user_text:
        break
