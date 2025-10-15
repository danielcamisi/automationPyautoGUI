import pyautogui
import time

pyautogui.hotkey('win', 'd')
time.sleep(0.5)
pyautogui.rightClick(x=500,y=300)
pyautogui.click(x=500,y=300)
pyautogui.doubleClick(x=500,y=300)