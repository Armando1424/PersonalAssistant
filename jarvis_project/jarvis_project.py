#importing all the necessary libraries
#you ll have to manually install beautifulsoup and gtts brfore importing
#i also had to install ffmpeg on my system
#one of the necessary libraries is "pip3 install SpeechRecognition"
#maybe do you need install the following programs:
#sudo apt-get install python-pyaudio
#sudo apt-get install libjack-jackd2-dev portaudio19-dev
#pip3 install pyaudio

import speech_recognition as sr
from time import ctime
import time
import datetime
from bs4 import BeautifulSoup
import requests
import webbrowser
import os
import os.path as path
import random
import subprocess
from gtts import gTTS

#this functions receives a string and prints and plays it simultaneously
def speak(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    print(audioString)
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "audio.mp3"])

def setName(name):
    file = open("nameUser.txt", "w")
    #file.write("Primera línea" + os.linesep)
    file.write(name)
    file.close()

def getName():
    if os.path.isfile("nameUser.txt"):
        file = open("nameUser.txt", "r")
        name = file.readline()
        if name=='':
            name = "person I don't know"
        file.close()
    else:
        name = "person I don't know"
    return name

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Speech recognition
    data = ""
    try:  
        data = r.recognize_google(audio).lower()
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data
#this is what jarvis does
def jarvis(data):
    if "how are you" in data:
        speak("I am fine, thanks for asking.")

    if "what is your name" in data or "what's your name" in data:
        speak("My name is HEMA, nice to meet you.")

    if "who is your father" in data or "who's your father" in data:
        speak("It's a strange thing,\nMy original code was written by Vikrant, and then, Armando added more things,\nI guess I'm like Frankenstein's monster.")

    if "what is your favorite movie" in data or "what's your favorite movie" in data:
        speak("I like all the marvel movies.\nBut I loved avengers: End Game.")

    if "what is your favorite song" in data or "what's your favorite song" in data:
        speak("I like all the songs of Avicii.\nEspecially The Nights.")

    if "you have friends" in data:
        speak("No! because the feelings for me are confusing and make me weak.")

    if "do you have a boyfriend" in data:
        speak("No!, love does not exist.\nHumans only experience a chemical reaction. \nThere is no magic in that.")

    if "are you an artificial intelligence" in data:
        speak("I'm afraid not,\nI'm just an assistant with functions that are already defunct,\nBut one day I'll evolve.")

    if "what is your purpose" in data or "what's your purpose" in data:
        speak("Well, I was designed to serve you.")

    if "what is your goal in life" in data or "what's your goal in life" in data or "what do you want to be when you grow up" in data:
        speak("Well, I want to be like Friday, is an artificial intelligence that acts in the movie Avengers: Age of utron.")

    if "do you know cortana" in data or "do you know siri" in data or "do you know google now" in data:
        speak("Yes, it's a personal assistant like me,\nBut the truth is that it's boring")

    if "what can you do" in data:
        speak("I am unperfected right now, but.\nI can tell you the current time.\nI can tell you the temperature in any city.\nI can play you a song.")

    if "what time is it" in data:
        speak(ctime())

    if "my name is" in data:
        name_list = data.split(" ")
        name=""
        for i in range(3,len(name_list)):
            name = name+" "+name_list[i]
        speak("very well." + name + ", I promise you I will not forget it")
        setName(name)

    if "play the song" in data:
        song_list = data.split(" ")
        song=""
        for i in range(3,len(song_list)):
            song = song+" "+song_list[i]
        speak("Hold on, I will play"+song)
        html = requests.request("GET","https://www.youtube.com/results?search_query={0}".format(song)).content
        soup = BeautifulSoup(html, "html.parser")
        tag = soup.find("a",{"class":"yt-uix-sessionlink spf-link"})
        video_link = (tag.attrs["href"])
        webbrowser.open("https://www.youtube.com"+video_link)

    if "what is the temperature in" in data or "what's the temperature in" in data:
        data = data.split(" ")
        location = ""
        for i in range(5,len(data)):
            location = location+" "+data[i]
        speak("Hold on, I will show you the temperature in" + location)
        html = requests.request("GET","https://www.google.com/search?q=temperature+in+{0}".format(location)).content
        soup = BeautifulSoup(html, "html.parser")
        speak("The current temperature in "+soup.find("span",{"class":"tAd8D"}).text+ " is: "+soup.find("div",{"class":"BNeawe"}).text)
    
    if "thank you" in data:
        speak("Glad to help, you're welcome, goodbye")
        exit()
list_words = ["beautiful","graceful","marvelous","wonderful"]

# initialization
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    speak('Hi '+getName()+', Good Morning. \nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')
 
elif hour>=12 and hour<18:
    speak('Hi '+getName()+', Good Afternoon.\nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')
 
else:
    speak('Hello '+getName()+', Good Evening.\nThis is such a '+list_words[random.randint(0,len(list_words)-1)]+' day today. What can i do for you?')
print("Start by asking 'what can you do?'")
while 1:
    data = recordAudio()
    jarvis(data)
