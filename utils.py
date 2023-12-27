import re
import time
import subprocess
import pyautogui
import pygetwindow as gw

from colorama import init, Fore

init(autoreset=True)

BROWSER_TITLE = 'Brave'

BROWSER_EXE = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"


def focus_browser_window(window):
    window.activate()
    window.restore()
    if not window.isMaximized:
        window.maximize()


def open_browser(is_private_tab=False):
    """
        Open the browser
    """
    browser_windows = gw.getWindowsWithTitle(BROWSER_TITLE)

    if not browser_windows:
        subprocess.Popen([BROWSER_EXE])

        if is_private_tab:
            time.sleep(.5)
            pyautogui.hotkey("ctrl", "shift", "n")

        return None

    current = 0

    tabs = []

    for window in browser_windows:
        focus_browser_window(window)

        pyautogui.hotkey("ctrl", "t")

        tabs.append(gw.getActiveWindow())

        current = current + 1

    open_tabs = [item for item in tabs if item.title == 'New Tab - Brave']
    private_tabs = [item for item in tabs if item.title ==
                    'New Private Tab - Brave']

    if len(private_tabs) == 0 and is_private_tab == True:
        focus_browser_window(open_tabs[0])
        time.sleep(.5)
        pyautogui.hotkey("ctrl", "shift", "n")
        time.sleep(.5)
        return None

    if len(open_tabs) > 0 and is_private_tab == False:
        if len(private_tabs) > 0:
            focus_browser_window(private_tabs[0])
            time.sleep(.5)
            pyautogui.hotkey("ctrl", "9")
            time.sleep(.3)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(.5)

        focus_browser_window(open_tabs[0])
        time.sleep(1)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(.2)
        pyautogui.hotkey("ctrl", "9")
        time.sleep(.2)
        pyautogui.hotkey("ctrl", "w")

    if len(private_tabs) > 0 and is_private_tab == True:
        if len(tabs) > 0:
            focus_browser_window(tabs[0])
            time.sleep(.5)
            pyautogui.hotkey("ctrl", "9")
            time.sleep(.3)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(.5)

        focus_browser_window(private_tabs[0])

        time.sleep(.2)
        if len(private_tabs) == 1:
            pyautogui.hotkey("ctrl", "t")

        time.sleep(1)
        pyautogui.hotkey("ctrl", "t")
        time.sleep(.2)
        pyautogui.hotkey("ctrl", "9")
        time.sleep(.2)
        pyautogui.hotkey("ctrl", "w")


"""
    ****************************
"""


def color_print(text, **kawrgs):
    """
        Changes print color
    """
    print(Fore.LIGHTGREEN_EX + text, **kawrgs)


"""
    ****************************
"""

regex = r"^(?:https:\/\/)?(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$"


def is_valid_domain(string):
    return re.match(regex, string) is not None
