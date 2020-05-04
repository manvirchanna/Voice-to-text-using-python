
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser 
import os
import smtplib
import random
import wolframalpha 
import requests


engine = pyttsx3.init('')
voices = engine.getProperty('')

engine.setProperty('voice', voices["Enter for voice code"].id)


def speak(audio):
    (engine.say(audio))
    (engine.runAndWait())


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")


def hello():
    wishMe()
    print("This is made by Manvir Singh. I can convert voice into text")
    speak("This is made by Manvir Singh. I can convert voice into text")


           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    hello()
    while True:
        query = takeCommand().lower()

        if 'stop' in query or 'bye' in query:

            speak("Bye, Have a nice day")
            exit()
        
        else:
            speak(query)    
      
