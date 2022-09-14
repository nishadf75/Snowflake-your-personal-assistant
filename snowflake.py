import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak("Good Evening!")
    speak('Hi mate')
    speak('I am your assistant jojo')
    speak('How can i help you')
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User Said:{query}\n")

        except Exception as e:
            print(e)
            print('say that again...')
            return 'None'
        return query
if __name__ == "__main__":
    wishMe()
    while True:
        if 1:
            query=takecommand().lower()
        if 'wikipedia' in query:
            speak("searching Wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'the time now' in query:
            strTime=datetime.datetime.now()
            time=strTime.strftime("%H:%M:%S")
            speak(f"sir, the time is {time}")
