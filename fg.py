#!/usr/bin/env python
# coding: utf-8

# In[3]:


import datetime
import pyttsx3 as pt
import pyaudio as py
import webbrowser as we
import pyjokes as pj
import speech_recognition as sr
def voice():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print(" SPEAK NOW..!")
        command.adjust_for_ambient_noise(source)
        audio=command.listen(source)
        try:
            print("Listening...")
            data=command.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not recognized, Ask again.. !")

def voice_text(x):
    engine=pt.init()
    #properties
    voices=engine.getProperty('voices')
    #setting property
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',180)
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':
        data1=voice().lower()
        if "your name" in data1:
            c1=" My name is Charlie"
            voice_text(c1)
        elif "first president" in data1:
            c2=" Dr. rajendra parsad is first president of india"
            voice_text(c2)
        elif 'time' in data1:
            c3=datetime.datetime.now().strftime("%I%M%p")
            voice_text(c3)
        elif 'sidhu' in data1:
            we.open("https://www.youtube.com/watch?v=h0x28vkqKrA")
        elif 'karan' in data1:
            we.open("https://www.youtube.com/watch?v=uR5_pWBs8Nw")
        elif 'joke' in data1:
            joke_1=pj.get_joke(language="en")
            voice_text(joke_1)
        else:
            print("I didn't understand")
    


# In[11]:


def voice_text(x):
    engine=pt.init()
    #properties
    voices=engine.getProperty('voices')
    #setting property
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',180)
    engine.say(x)
    engine.runAndWait()
if __name__ == '__main__':
        data1=voice().lower()
        if "your name" in data1:
            c1=" My name is Charlie"
            voice_text(c1)
        elif "first president" in data1:
            c2=" Dr. rajendra parsad is first president of india"
            voice_text(c2)
        elif 'time' in data1:
            c3=datetime.datetime.now().strftime("%I%M%p")
            voice_text(c3)
        elif 'sidhu' in data1:
            we.open("https://www.youtube.com/watch?v=h0x28vkqKrA")
        elif 'karan' in data1:
            we.open("https://www.youtube.com/watch?v=uR5_pWBs8Nw")
        elif 'joke' in data1:
            joke_1=pj.get_joke(language="en")
            voice_text(joke_1)
        else:
            print("I didn't understand")
    


# In[ ]:




