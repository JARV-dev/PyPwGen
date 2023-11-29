import secrets
import string
import PySimpleGUI as sg
import pyperclip
import time
import os

#def font size
font_config = {'font': ('Constantia', 20)}

def generate_password(length, use_letters, use_digits, use_special_chars):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    selection_list = ""
    if use_letters:
        selection_list += letters
    if use_digits:
        selection_list += digits
    if use_special_chars:
        selection_list += special_chars

    if not selection_list:
        # If none of the options are selected, use all character types
        selection_list = letters + digits + special_chars

    return "".join(secrets.choice(selection_list) for _ in range(length))

def main():
    text_element = lambda text: sg.Text(text, **font_config)
    input_element = lambda size: sg.InputText(size=size, **font_config)

    layout = [
        [sg.Text('Select character types:', **font_config)],
        [sg.Checkbox('Letters', key='-LETTERS-', **font_config)],
        [sg.Checkbox('Digits', key='-DIGITS-', **font_config)],
        [sg.Checkbox('Special Characters', key='-SPECIAL-', **font_config)],
        [sg.Text('Password Length:'), sg.InputText(size=(5, 1), key='-LENGTH-', **font_config)],
        [sg.Text('Website:'), sg.InputText(size=(5, 1), key='-WEBSITE-', **font_config)],
        [sg.Button('Generate Password', **font_config), sg.Button('Exit', **font_config)],
    ]

    window = sg.Window('Password Generator', layout, **font_config)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Generate Password':
            try:
                use_letters = values['-LETTERS-']
                use_digits = values['-DIGITS-']
                use_special_chars = values['-SPECIAL-']
                length = int(values['-LENGTH-'])
                website = values['-WEBSITE-']

                password = generate_password(length, use_letters, use_digits, use_special_chars)

                # You can add your code for where_used here if needed

                # Outputs the generated password to a notepad in the same dir as the program
                with open("Password.txt", "a") as ff:
                    print(password, " --- ", website, file=ff)

                # Copy the password to the user's clipboard
                pyperclip.copy(password)

                sg.popup_ok('Password generated successfully!\n\n', f'Password: {password}\nCopied to clipboard.\n\n', 'Developed by JARV-Dev', **font_config)

            except ValueError:
                sg.popup_error('Please enter a valid number for password length.', **font_config)

    window.close()

if __name__ == "__main__":
    main()