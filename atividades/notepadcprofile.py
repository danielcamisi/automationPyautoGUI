import pyautogui
import time
import subprocess

def open_notepad():
    subprocess.Popen("notepad.exe")
    time.sleep(1.5)

def text_write():
    texto = "Ola, teste de automacoes\n" * 4
    pyautogui.write(texto, interval=0.04)

def save_file():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.write("arquivoss", interval=0.04)
    pyautogui.press('enter')

def close_notepad():
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')

def all_func():
    open_notepad()
    text_write()
    save_file()
    close_notepad()

if __name__ == "__main__":
    import cProfile
    cProfile.run("all_func()")