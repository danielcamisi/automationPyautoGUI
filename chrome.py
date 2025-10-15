import pyautogui
import time
import subprocess
import pyperclip

pyautogui.hotkey('win', 'r')

pyautogui.write('chrome.exe')

pyautogui.press('Enter')

time.sleep(1)

pyperclip.copy('www.youtube.com.br')
pyautogui.hotkey('ctrl', 'v')

time.sleep(0.2)

pyautogui.press('Enter')

time.sleep(0.5)

pyautogui.click(400, 150)

pyperclip.copy("Senac")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')