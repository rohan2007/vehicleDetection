import pyautogui
import time

# !!!!! ATTENTION !!!!!

# you have to edit pyautogui.moveTo(50,160) file according to your screen

time.sleep(10)

pyautogui.moveTo(50,160)

while True:
    time.sleep(1)
    pyautogui.click()
