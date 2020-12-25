import pyautogui
import time

# !!!!! ATTENTION !!!!!
# you have to make moveTo according to your screen reader

time.sleep(10)

pyautogui.moveTo(50,160)

while True:
    time.sleep(1)
    pyautogui.click()
