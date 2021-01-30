import pyautogui
import time

time.sleep 

f = open("bot.txt", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")