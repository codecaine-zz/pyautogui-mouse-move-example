#move mouse every 60 seconds on screen to x, y position
import pyautogui
import time


if __name__ == '__main__':
    pyautogui.PAUSE = 60
    pyautogui.FAILSAFE = True

    while True:
        pyautogui.moveTo(x=200,y=50)
        pyautogui.moveTo(x=200,y=100)