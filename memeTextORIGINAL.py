from pynput import keyboard
import pyautogui
import pyperclip
import time
import random

text = ""
memedText = []
memedTextStr = ""

COMBINATIONS = [
    {keyboard.KeyCode(vk=113)}
]

current = set()

def copy():
    global text
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", 'c')
    time.sleep(0.1)
    text = pyperclip.paste()
    print(text)

def randomMemeText(text):
    global memedTextStr
    for c in text:
        upperLower = random.randint(0, 1)
        if upperLower == 0:
            memedText.append(c.lower())
        if upperLower == 1:
            memedText.append(c.upper())
    memedTextStr = "".join(memedText)
    
def memeText(text):
    global memedTextStr
    upper = False
    for c in text:
        if upper == True:
            memedText.append(c.upper())
            if c != ' ':
                upper = False
        else:
            memedText.append(c.lower())
            if c != ' ':
                upper = True
    memedTextStr = "".join(memedText)

def keyboardWrite():
    global memedTextStr
    pyautogui.press("backspace")
    time.sleep(1)
    pyautogui.write(memedTextStr)

def memeify():
    global memedTextStr
    global text
    global memedText

    copy()
    randomMemeText(text)
    #memeText(text)
    keyboardWrite()
    
    print(memedTextStr)
    text = ""
    memedText = []
    memedTextStr = ""
    
def on_press(key):

    if str(key) == "Key.f2":
        memeify()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()