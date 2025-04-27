import speech_recognition as sr # type: ignore
import webbrowser
import pyttsx3 # type: ignore
import music_library
from openai import OpenAI # type: ignore
from api_key import api_key
engine = pyttsx3.init() # created an object of init class

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_openai(c):
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1",
        input= c
    )

    speak(response.output_text)

def process_command(c):
    if 'open google' in c:
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in c:
        webbrowser.open("https://www.youtube.com")
    elif 'open facebook' in c:
        webbrowser.open("https://www.facebook.com")
    elif 'play' in c:
        webbrowser.open(music_library.music[c.split(' ')[1]])
    elif 'exit' in c:
        exit()
    else:
        process_openai(c)

if __name__ == '__main__':
    speak("Initiating jarvis ...")
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=4,phrase_time_limit=10)
                print("Recognizing....")
                triggered_word = r.recognize_google(audio).lower()
                print(triggered_word)
                if 'jarvis' in triggered_word:
                    speak("Hello User! Please give any command")
                    try:
                        print("Listening for command ....")
                        audio = r.listen(source,timeout=2,phrase_time_limit=10)
                        command_text = r.recognize_google(audio).lower()
                        process_command(command_text)
                    except Exception as e:
                        print(e)
                else:
                    speak("Not able to interpret . Please speak again")
        except Exception as e:
            print(e)