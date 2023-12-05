#secrets for randomly generating the characters
import secrets
#string library
import string
#gui library
import PySimpleGUI as sg
#to automatically copy to clipboard
import pyperclip
#to calc. the elapsed time
import time
#to create the .txt file
import os
#to bundle the icon with the --onefile program
import sys

#sets the icon path
icon_path = 'C:/Users/JARV Dev/Desktop/PyPwGen/PW.GEN.by.JARV.ico'

#def font size
font_config = {'font': ('Arial', 40)}

#set gui theme and global icon
sg.theme_global('PythonPlus')
sg.set_global_icon(icon_path)

#define the universe of characters
def generate_password(length, use_letters, use_digits, use_special_chars):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
#work out the user character selection
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
#generate and join all the random characters
    return "".join(secrets.choice(selection_list) for _ in range(length))

def main():
    text_element = lambda text: sg.Text(text, **font_config)
    input_element = lambda size: sg.InputText(size=size, **font_config)
#set the program layout
    
    layout = [
        [sg.Push(), sg.Text('Python Based Password Generator by JARV-Dev\n', font={'Arial', 5}), sg.Push()],
        [sg.Push(), sg.Text('Select the desired character types:\n', **font_config), sg.Push()],
        [sg.Push(), sg.Checkbox('Letters', key='-LETTERS-', tooltip='Eg. A,b,c,d...', **font_config), sg.Push(), sg.Checkbox('Digits', key='-DIGITS-', tooltip='Eg. 1,2,3,4...', **font_config), sg.Push(), sg.Checkbox('Special Characters', key='-SPECIAL-', tooltip='Eg. !,#,$,%...', **font_config), sg.Push()],
        [sg.Text('')],
        [sg.Push(), sg.Text('Password Length:'), sg.InputText(size=(22, 1), tooltip='How many characters should the password have?', justification='l', key='-LENGTH-', **font_config)],
        [sg.Push(), sg.Text('Website:'), sg.InputText(size=(22, 1), tooltip='This will be stored with the password locally in the generated .txt file', justification='l', key='-WEBSITE-', **font_config)],
        [sg.Text('')],
        [sg.Button('About', button_color='White', tooltip='Displays information about the program provided by the developer'), sg.Push(), sg.Button('Generate Password', button_color='Green', **font_config, tooltip='Makes the magic happen'), sg.Push(), sg.Button('Exit', button_color='Red', **font_config, tooltip='Closes the program')],
    ]
#creates the window
    window = sg.Window('Password Generator by JARV-Dev', layout, resizable=False, auto_size_buttons=True, **font_config)
#reads the values
    while True:
        event, values = window.read()
#close the program
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        #about 'button'
        elif event in (sg.Window, 'About'):
            sg.popup_ok('This program is my first python project and was created solely for practice purposes.\n\nIt does not have the capability to send or recieve any data and therefore its use is completely safe security-wise.\n\nWith this being said the only security risk would be your computer being infected with malware (which would not have anything to do with my program itself).\n\n If you have any questions or need help don''t hesitate messaging me on discord: jarvpt', title='About')
        #generate password 'button'
        elif event == 'Generate Password':
            try:
                use_letters = values['-LETTERS-']
                use_digits = values['-DIGITS-']
                use_special_chars = values['-SPECIAL-']
                length = int(values['-LENGTH-'])
                website = values['-WEBSITE-']

                password = generate_password(length, use_letters, use_digits, use_special_chars)

                # Outputs the generated password to a notepad in the same dir as the program
                with open("Passwords.txt", "a") as ff:
                    print(password, " ::::: ", website, "\n", file=ff)

                # Copy the password to the user's clipboard
                pyperclip.copy(password)

                sg.popup_ok('Password generated successfully!\n\n', f'Password: {password}\nCopied to clipboard.\n\n', 'Developed by JARV-Dev', **font_config)

            except ValueError:
                sg.popup_ok('Please enter a valid number for password length.', title='Houston, we have a problem', **font_config)

    window.close()

if __name__ == "__main__":
    main()