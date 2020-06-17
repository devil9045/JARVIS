import speech_recognition as sr
import wolframalpha
import os
import playsound
from gtts import gTTS
from selenium import webdriver
import pyaudio
import speaks

num = 1


def assistant_speakes(output):
    global num

    num += 1
    print("JARVIS : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        audio = rObject.listen(source, phrase_time_limit=5)
        print("Stop.")

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        assistant_speakes("Could not understand your audio, Please try again !")
        return 0


if __name__ == "__main__":
    assistant_speakes("What's your name, Master?")
    name = ''
    name = get_audio()
    assistant_speakes("Hello, " + str(name).upper() + '.')

    while 1:

        assistant_speakes("What can I do for you?")
        text = str(get_audio())

        speaks.process_text(text)



