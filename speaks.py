import wolframalpha

import calc
from jarvis import assistant_speakes, get_audio
import search
import datetime

def process_text(text):
    try:
        if 'web' in text.lower() or 'play' in text.lower():
            search.search_web(text)

        elif "who are you" in text.lower() or "define yourself" in text.lower():
            speak = 'HELLO I AM JARVIS YOUR PERSONAL ASSISTANT'
            assistant_speakes(speak)

        elif "who made you" in text.lower() or "created you" in text.lower():
            speak = "I have been created by master Henish."
            assistant_speakes(speak)

        elif 'open' in text.lower():
            calc.open_application(text)

        elif 'date' in text.lower() or 'today date' in text.lower():
            date = datetime.datetime.date().today()
            assistant_speakes(date)

        elif 'time' in text.lower() or 'current time' in text.lower() or 'what is time' in text.lower():
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
