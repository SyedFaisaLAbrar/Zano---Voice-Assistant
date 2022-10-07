import random
import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
# import pywhatkit
import pyautogui
import shutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 155)

time_searches = ["what's the time", "what time is it", "tell me the time", "what time it is"]
pmList = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def speak(query):
    engine.say(query)
    engine.runAndWait()


def speakTime(co_mmand):
    for x in time_searches:
            if x in co_mmand:
                Time = datetime.datetime.now().strftime("%H:%M:%S")
                ntime = Time.split(":")
                if ntime[0] in pmList:
                    speak(f"It's {int(ntime[0])-12} {ntime[1]} PM")
                elif ntime[0] == "24" or ntime[0] == "00":
                    speak(f"It's {12} {ntime[1]} AM")
                elif ntime[0] == "12":
                    speak(f"It's {12} {ntime[1]} PM")
                else:
                    speak(f"It's {int(ntime[0])} {ntime[1]} PM")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning .....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-US")
        print("You Searched : ", query)
    except Exception as e:
        print("Please say that again")
        return "None"
    return query


def take_secrete_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning....")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-US")
        print("You Searched : ", query)
    except Exception as e:
        return "None"
    return query


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir.")


def youtube_actions(query):
    if "open youtube" in query:
        url = "youtube.com"
        webbrowser.get(chrome_path).open(url)
    elif "play" in query:
        n1 = query.replace("play", "")
        n2 = n1.replace("on youtube", "")
        webbrowser.get(chrome_path).open(f"https://youtube.com/results?search_query={n2}")


def takeSS():
    files = os.listdir()
    rand = random.randint(11111, 111111)
    lst = [x for x in files if os.path.splitext(x)[1] == ".png"]
    list_int = []
    for file in lst:
        x = file.split(".")
        list_int.append(int(x[0]))
    if rand in list_int:
        rand+=max(list_int)
        screen_shot = pyautogui.screenshot()
        screen_shot.save(f"{rand}.png")
    else:
        screen_shot = pyautogui.screenshot()
        screen_shot.save(f"{rand}.png")


def clean_folder(folder_path):
    files = os.listdir(folder_path)
    files.remove("Automatic Folder Cleaner.py")
    path_f = folder_path

    def makeNewDir(file_name):
        n_path = os.path.join(path_f, file_name)
        if not os.path.exists(n_path):
            os.makedirs(n_path)

    def getFiles(formatlist):
        return [file for file in files if os.path.splitext(file)[1].lower() in formatlist]

    def move(present, to):
        shutil.move(present, to)

    makeNewDir("Images")
    makeNewDir("Media")
    makeNewDir("Documents")
    makeNewDir("Others")

    imageFormat = [".png", ".jpg", ".jpeg", ".ico", ".svg", ".gif"]
    docFormat = [".doc", ".docx", ".pdf", ".ppt", ".txt", ".xls"]
    mediaFormat = [".mp3", ".mp4", ".mkv", ".avi", ".wmv", ".mov", ".avchd", "webm", ".mpeg-2"]
    otherFormat = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imageFormat) and (ext not in mediaFormat) and (ext not in docFormat) and os.path.isfile(file):
            otherFormat.append(ext)

    images = getFiles(imageFormat)
    media = getFiles(mediaFormat)
    documents = getFiles(docFormat)
    others = getFiles(otherFormat)

    for img in images:
        move(f"{path_f}\\{img}", f"{path_f}\\Images\\{img}")
    for med in media:
        move(f"{path_f}\\{med}", f"{path_f}\\Media\\{med}")
    for doc in documents:
        move(f"{path_f}\\{doc}", f"{path_f}\\Documents\\{doc}")
    for oth in others:
        move(f"{path_f}\\{oth}", f"{path_f}\\Others\\{oth}")


def whatsapp_manager(query):
    webbrowser.get(chrome_path).open("whatsapp.com")


if __name__ == '__main__':

    greetings()

    while True:
        secrete_command = take_secrete_command().lower()
        if "zano" in secrete_command:
            print("Initializing Zano.....")
            speak("Yes?")

            command = take_command().lower()
            if "wikipedia" in command:
                command = command.replace("wikipedia", "")
                result = wikipedia.summary(command, sentences=2)
                speak("According to wikipedia")
                speak(result)
            elif "time" in command:
                speakTime()
            elif "youtube" in command:
                youtube_actions(command)
            elif "take screenshot" in command:
                takeSS()
            elif "open whatsapp" in command:
                whatsapp_manager(command)
            elif "open chrome" or "open google" in command:
                webbrowser.open("google.com")
            elif "open photoshop" in command:
                os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2022\\Photoshop.exe")
            elif "open pycharm" in command:
                os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.2\\bin\\pycharm64.exe")
            elif "open gmail" in command:
                webbrowser.open("gmail.com")
            elif "open control panel" in command:
                os.startfile("C:\\Users\\Syed Faisal Abrar\\AppData\\Roaming\\Microsoft\\Windows\\"
                             "Start Menu\\Programs\\System Tools\\Control Panel.lnk")
            elif "clean a folder" in command:
                speak("Give me the path of that folder")
                path = input(str("Enter path of folder : "))

                clean_folder(path)
            elif "who are you" or "what is your name" or "what's your name":
                speak("I am Zano. I was basically created to assist humans.")
            elif "your father name" or "your mother name" or "do you have siblings":
                speak("I have no family. I am actually an AI based virtual assistant created by Fzotix.")
            elif "shutdown" or "shutdown system" or "shutdown my computer" in command:
                speak("Shutting down")
                os.system("shutdown /s /t 1")
