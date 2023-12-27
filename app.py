
import time
import pyautogui
from utils import open_browser, color_print

user_input = ""

help_text = """
Learn to use the followings in order use hanlebar better

open sites with:
    -os site_name 
        Example: -os youtube
        default supported sites are:
            - youtube.com 
            - imdb.com 
            - google.com   
            - yahoo.com   
            - healthline.com    
            - developer.mozilla.org 

        for other sites you can use the following:
            -osm site_domain
            Example: -osm nytimes.com/international
        
        to open sites in a private tab use the following:
            -os site_name -p 
                Example: -os youtube -p
            -osm site_domain -p
                Example: -osm nytimes.com/international -p
"""

def open_world():
    if "youtube" in user_input:
        open_browser()
        time.sleep(1)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(1)
        pyautogui.hotkey("alt", "d")
        pyautogui.write("https://www.youtube.com/")
        pyautogui.press("enter")


def show_help():
    color_print(help_text)


def app(u_input):
    global user_input
    user_input = str(u_input).lower()

    if "--help" in user_input:
        show_help()

    elif "-os" in user_input:
        open_world()
    else:
        color_print("Miss typed?, to learn more write --help")
        print()
