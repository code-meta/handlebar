import pyautogui

"""
    methods for typing site urls
"""


def youtube():
    pyautogui.write("https://www.youtube.com/")
    pyautogui.press("enter")


def imdb():
    pyautogui.write("https://imdb.com/")
    pyautogui.press("enter")


def google():
    pyautogui.write("https://google.com/")
    pyautogui.press("enter")


def yahoo():
    pyautogui.write("https://yahoo.com/")
    pyautogui.press("enter")


def healthline():
    pyautogui.write("https://healthline.com/")
    pyautogui.press("enter")


def mdn():
    pyautogui.write("https://developer.mozilla.org/")
    pyautogui.press("enter")


def unknown_site(url):
    pyautogui.write(url)
    pyautogui.press("enter")
