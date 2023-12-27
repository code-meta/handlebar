from app import app
from utils import color_print


# # ask the user what they want
greet = """
Welcome back, this is handlebar your personal
assistant for handling common task like 
open websites or apps.
to open sites like youtube write \"-o youtube\".
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
        color_print("What is it you want? ", end="")
        user_input = input().lower()
        app(user_input)
except:
    print("\n\n")
    color_print("You can write \"q\" to exit.")