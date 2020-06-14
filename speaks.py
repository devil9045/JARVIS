import wolframalpha

import calc
from jarvis import assistant_speakes, get_audio
import search
import datetime

def process_text(text):
    try:
        if 'web' in text or 'play' in text:
            search.search_web(text)

        elif "who are you" in text or "define yourself" in text:
            speak = 'HELLO I AM JARVIS YOUR PERSONAL ASSISTANT'
            assistant_speakes(speak)

        elif "who made you" in text or "created you" in text:
            speak = "I have been created by master Henish."
            assistant_speakes(speak)

        elif 'open' in text:
            calc.open_application(text)

        elif 'date' in text or 'today date' in text:
            date = datetime.datetime.date().today()
            assistant_speakes(date)

        elif 'time' in text or 'current time' in text or 'what is time' in text:
            time = datetime.datetime.today().time().replace(microsecond=0)
            assistant_speakes(time)

        else:

            assistant_speakes("I can search the web for you , Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search.search_web(text)
            else:
                exit()

    except:
        assistant_speakes("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search.search_web(text)
