import pyautogui
import subprocess
import time

pyautogui.hotkey('win','r')
pyautogui.write('cmd')
pyautogui.press('enter')

time.sleep(0.5)

pyautogui.write("npm install @angular/cli")
time.sleep(0.2)
pyautogui.press('Enter')