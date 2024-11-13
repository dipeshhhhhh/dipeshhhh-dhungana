import os

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    # Get user input with a prompt
    return input(prompt)