import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening")    
    if __name__=="__main__":
       speak("I am Javis sir . please tell me how can i help you")  

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)

        print("say that agian please sir...")
        speak("say that agian please sir...")
        return "none"
    return query




if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=12)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")    
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'open ganna' in query:
            webbrowser.open("gaana.com") 
        #elif 'play music' in query:
            #music_folder = "C:\Users\rk001\Music\tillu"
            #random_music = (os.listdir(music_folder))
            #os.startfile(os.path.join(music_folder,random_music))

#def set_reminder(activity:str, hour:int, minute:int):
    current_time = datetime.datetime.now()
    reminder_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if reminder_time < current_time:
        reminder_time = reminder_time + datetime.timedelta(days=1)
    speak(f"Reminder set for {activity} at {reminder_time.strftime('%I:%M %p')}")
    time.sleep(60)
    if datetime.datetime.now() > reminder_time:
        speak(f"Reminder: {activity}")
#set_reminder("Take Medication", 8, 0)
#set_reminder("Exercise", 15, 30)  
       

          