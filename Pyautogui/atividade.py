import pyautogui
import time
import subprocess

pyautogui.hotkey('win', 'r')
subprocess.Popen("notepad.exe")
time.sleep(0.3)
pyautogui.hotkey("ctrl","s")
pyautogui.write("Minha_Nota")
time.sleep(0.3)
pyautogui.press("enter")
