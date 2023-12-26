
import subprocess
import pygetwindow as gw

BROWSER_TITLE = 'Brave'

BROWSER_EXE = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"


def open_browser():
    browser_windows = gw.getWindowsWithTitle(BROWSER_TITLE)

    if browser_windows:
        current = 0
        for window in browser_windows:
            if "Private" not in window.title:
                browser_windows[current].activate()
                browser_windows[current].restore()
                browser_windows[current].maximize()

            current = current + 1
    else:
        subprocess.Popen([BROWSER_EXE])
