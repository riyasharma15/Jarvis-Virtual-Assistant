import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import smtplib
import pywhatkit as kit
import cv2
import random
from requests import get
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


# print(voices[1].id)

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour <= 16:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("I am Jarvis. Please tell me how may I help you.")
    speak("I am Jarvis. Please tell me how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\nListening...")
        r.energy_threshold = 2318
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}")
    except Exception as e:
        print(f"Say that again please!")
        speak("Say that again please!")
        return "None"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('riyasharma1727@gmail.com', 'riya@2000')
    server.sendmail('riyasharma1727@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open('youtube.com')
            # time.sleep(50)
        elif 'open notepad' in query:
            path = "C:\\windows\\system32\\notepad.exe"
            os.startfile(path)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open stack over flow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = "C:\\Users\\hp\\Desktop\\Music"
            songs = os.listdir(music_dir)
            # print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'wikipedia' in query:
            print("Searching wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia...")
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open visual studio code' in query:
            path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'send email' in query:
            try:
                print("To whom you want to send the email?")
                speak("To whom you want to send the email?")
                to = input("Enter email here: ")
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                while content == "None":
                    content = takeCommand()
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print('Sorry, I am not able to send the email at this moment')
                speak('Sorry, I am not able to send the email at this moment')
        elif 'search' in query:
            print("What do you want to search for?")
            speak("What do you want to search for?")
            search = takeCommand()
            while search == "None":
                search = takeCommand().lower()
            webbrowser.open(f"{search}")
        elif 'find location' in query:
            print("What is the location?")
            speak("What is the location?")
            location = takeCommand()
            while location == "None":
                location = takeCommand().lower()
            url = "https://google.nl/maps/place/" + location + "/&amp;"
            webbrowser.get().open(url)
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xFF == ord(' '):
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play song on youtube' in query:
            print("Which song do you want to listen?")
            speak("Which song do you want to listen?")
            song = takeCommand().lower()
            kit.playonyt(song)
        elif 'play songs on youtube' in query:
            print("Which song do you want to listen?")
            speak("Which song do you want to listen?")
            song = takeCommand().lower()
            kit.playonyt(song)
        elif 'instagram profile' in query or 'profile on instagram' in query:
            print("Please enter the username")
            speak("Please enter the username")
            name = input("Enter username here: ")
            webbrowser.open(f"instagram.com/{name}")
        elif 'exit' in query:
            sys.exit()