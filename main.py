from app import app
from utils import color_print
from pyautogui import FailSafeException

# # ask the user what they want
greet = """
Welcome back, this is handlebar your personal
assistant for handling common task like 
open websites or apps.
to open sites like youtube write \"youtube\".
to learn more about the features write \"--help".
"""

bicycle = """
          __o
  _ `-    _ \<_
 ( O )----( O )
"""
color_print(bicycle)

color_print(greet)

user_input = ""

try:

    while user_input != 'q':
        color_print("What action do you want to perform?")
        user_input = input().lower()
        app(user_input)

except KeyboardInterrupt:
    print("\n\n")
    color_print("You can write \"q\" to exit.")
except FailSafeException:
    msg = """
    Please don't use the mouse after commanding
    wait until the action is done.
"""
    color_print(msg)

except Exception as e:
    print("\n\n")
    print(e)
    color_print("Unexpacted error occurred.")
