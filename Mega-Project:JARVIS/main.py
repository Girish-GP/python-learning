
import speech_recognition as sr # type: ignore , speech recognition module
import webbrowser # webbrowser module imported for opening the sites
import pyttsx3 # type: ignore , text to speech module 
import musicLibrary

engine = pyttsx3.init() # created a object engine which has access to all classes and methods of pyttsx3

def speak(text): #speak function to speak text
    engine.say(text) # say fucntion which performs the operation of speaking
    engine.runAndWait() # function which completes the process above it

def process_command(c):
    if 'open youtube' in c.lower():
        webbrowser.open('https://www.youtube.com') #using webbrowser open method to open site
    elif 'open google' in c.lower():
        webbrowser.open('https://www.google.com')
    elif c.lower().startswith('play'):
        link = musicLibrary.music[c.lower().split(' ')[1]]
        webbrowser.open(link)
    elif 'exit' in c.lower():
        speak("Goodbye")
        exit()
    else:
        speak("Cant understand given command . Pls try some other command")

if __name__ == "__main__":
    speak("Initializing Jarvis....") # starting jarvis

    while True: # for continous execution
        try:
            r = sr.Recognizer() # created object r using Recognizer class
            with sr.Microphone() as source: # opening microphone and assigned the audio stream to source object
                audio = r.listen(source,timeout=2,phrase_time_limit=1) #listen to the source
                try:
                    trigger_word = r.recognize_google(audio)
                    if 'jarvis' in trigger_word:  # If the trigger word is detected
                        speak("Yes, how can I help?")
                        print("Listening for command...")
                        command = r.listen(source,timeout=2,phrase_time_limit=1) #listen to the command
                        print("Recognizing....")
                        temp = r.recognize_google(command) # recognize the command
                        process_command(temp) # process the command
                    else:
                        print("Not able to interpret the command")
                except Exception as e:
                    print(e)
        

        except Exception as e:
            print(e)
