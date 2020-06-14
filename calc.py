import os

from img2pdf import assistant_speakes


def open_application(text):

    if "chrome" in str(text).lower():
        assistant_speakes("Google Chrome")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
        return

    elif "wordpad" in str(text).lower():
        assistant_speakes("Opening Wordpad")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Wordpad.lnk")
        return

    elif "paint" in str(text).lower():
        assistant_speakes("Opening Paint")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint.lnk")
        return

    else:

        assistant_speakes("Application not available")
        return


