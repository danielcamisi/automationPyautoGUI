import pyautogui
import time

print("Pressione CTRL + C para parar.")
while True:
    x,y = pyautogui.position()
    print(f"Posição atual do mouse: X={x} Y={y}")
    time.sleep(0.1)