
import time
import pyautogui
from utils import open_browser, color_print

user_input = ""


def open_world():
    if "youtube" in user_input:
        open_browser()
        time.sleep(1)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(1)
        pyautogui.hotkey("alt", "d")
        pyautogui.write("https://www.youtube.com/")
        pyautogui.press("enter")


def app(u_input):
    global user_input
    user_input = u_input

    if "-o" in user_input:
        open_world()
    else:
        color_print("Miss typed?, to learn more write --help")
        print()
