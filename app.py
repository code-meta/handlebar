
import time
import pyautogui
from utils import open_browser

user_input = ""


def open_world():
    if "youtube" in user_input:
        open_browser()
        time.sleep(2)
        pyautogui.hotkey("Ctrl", "T")
        time.sleep(3)
        pyautogui.hotkey("Alt", "D")
        pyautogui.write("youtube.com")
        pyautogui.press("enter")


def app(u_input):
    global user_input
    user_input = u_input

    if "open" in user_input:
        open_world()
    else:
        print("ohh")
