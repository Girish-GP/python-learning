import speech_recognition as sr # type: ignore
import webbrowser
import pyttsx3 # type: ignore

speech_recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__": # when the file is directly executed
    speak("Initializing Jarvis...")
    while True:
        #listen for wake word Jarvis
        r = sr.Recognizer() #create a object using Recognizer class 
        with sr.Microphone() as source:
            print("Listening")
            audio = r.listen(source)

            #recognize
            # Recognize speech using Google Web Speech API
            try:
                print("You said: " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")




import speech_recognition as sr
import pyttsx3
import webbrowser
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if 'open google' in c.lower():
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://www.facebook.com")
    else:
        speak("Sorry i cant understand your command")


if __name__ == '__main__':
    speak("Initiating jarvis...")
    while True:
        r = sr.Recognizer()
        try:
             with sr.Microphone() as source:
                 print("Listening....")
                 audio = r.listen(source,timeout=2,phrase_time_limit=1)
                 print("Recognizing....")
                 temp = r.recognize_google(audio)
                 if temp.lower() == 'jarvis':
                     command = r.listen(source)
                     process_command(command)
                     
                     
        except Exception as e:
            print(e)

    

