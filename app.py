
import time
import pyautogui

from utils import open_browser, color_print

from settings import SITE, DEFAULT_SITES, HELP_TEXT

from services import youtube, google, yahoo, mdn, healthline, imdb, unknown_site

user_input = ""


def focus_url_bar():
    time.sleep(1.5)
    pyautogui.hotkey("alt", "d")


def open_site():
    is_private_tab = False

    if len(user_input) >= 3 and user_input[2] == "-p":
        is_private_tab = True

    try:
        site = DEFAULT_SITES.index(user_input[1])

        open_browser(is_private_tab)
        focus_url_bar()

        if SITE.YOUTUBE == DEFAULT_SITES[site]:
            youtube()
            return None

        if SITE.IMDB == DEFAULT_SITES[site]:
            imdb()
            return None

        if SITE.GOOGLE == DEFAULT_SITES[site]:
            google()
            return None

        if SITE.YAHOO == DEFAULT_SITES[site]:
            yahoo()
            return None

        if SITE.HEALTHLINE == DEFAULT_SITES[site]:
            healthline()
            return None

        if SITE.MDN == DEFAULT_SITES[site]:
            mdn()
            return None

    except ValueError:
        if "-osm" != user_input[0]:
            color_print("Unknown site use -osm for custom sites.\n")
            return None

        open_browser(is_private_tab)
        focus_url_bar()
        unknown_site(user_input[1])


def app(u_input):
    global user_input
    user_input = str(u_input).strip().split(" ")

    if "--help" == user_input[0]:
        color_print(HELP_TEXT)
        return None

    if not len(user_input) >= 2:
        color_print("Miss typed, please try again.\n")
        return None

    elif "-os" == user_input[0] or "-osm" == user_input[0]:
        open_site()

    else:
        color_print("Miss typed?, to learn more write --help")
        print()
