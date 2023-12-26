from app import app

# # ask the user what they want
user_input = ""

while user_input != 'q':
    user_input = input("What is it you want? ").lower()
    app(user_input)