from app import app
from utils import color_print


# # ask the user what they want
user_input = ""

while user_input != 'q':
    color_print("What is it you want? ", end="")
    user_input = input().lower()
    app(user_input)
