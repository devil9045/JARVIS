from selenium.webdriver.chrome import webdriver

from jarvis import assistant_speakes


def search_web(text):
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in str(text.lower()):
        assistant_speakes("Opening in Youtube")
        indx = text.lower().split().index('youtube')
        query = text.split()[indx + 1:]
        driver.get("https://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in str(text.lower()):
        assistant_speakes("Opening Wikipedia")
        indx = text.lower().split().index('wikipedia')
        query = text.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in str(text):

            indx = text.lower().split().index('google')
            query = text.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in str(text):
            indx = text.lower().split().index('google')
            query = text.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:
            driver.get("https://www.google.com/search?q =" + '+'.join(text.split()))

        return

