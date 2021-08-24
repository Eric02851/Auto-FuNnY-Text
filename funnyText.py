from pynput import keyboard
import sys
import pyautogui
import pyperclip
import random

if sys.platform == "darwin":
    key = '<cmd>+<shift>+f'
else:
    key = '<ctrl>+<shift>+f'

def copy():
    keys = ['f', 'command', 'shift']
    for key in keys:
        pyautogui.keyUp(key)

    pyautogui.hotkey("command", 'c')
    pyautogui.keyUp('c')
    text = pyperclip.paste()

    return text

def randomize(text):
    funnyString = ""
    for c in text:
        if random.randint(0, 1) == 0:
            funnyString += c.upper()
        else:
            funnyString += c.lower()

    return funnyString

def funnyPattern(text):
    upper = True
    funnyString = ""
    for c in text:
        if c == ' ':
            funnyString += ' '
            continue
        if upper == True:
            funnyString += c.upper()
            upper = False
        else:
            funnyString += c.lower()
            upper = True

    return funnyString

def on_activate_funny():
    text = copy()
    funnyString = randomize(text)
    #funnyString = funnyPattern(text) #uncomment for upper lower pattern
    print(funnyString)

    pyperclip.copy(funnyString)
    pyautogui.hotkey("command", 'v')

with keyboard.GlobalHotKeys({key: on_activate_funny}) as l:
    l.join()