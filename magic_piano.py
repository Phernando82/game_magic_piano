# https://gameforge.com/en-US/littlegames/magic-piano-tiles/#

import webbrowser
import pyautogui
import keyboard
from time import sleep
import win32api # pip install pywin32
import win32con # win32 clica mais rápido que o pyautogui

webbrowser.open('https://gameforge.com/en-US/littlegames/magic-piano-tiles/#')

sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

click(636,542)
sleep(2)
click(638,493)
sleep(1)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(501,396, (0,0,0)):
        click(501,396)
        # sleep(0.01)
    if pyautogui.pixelMatchesColor(596,386, (0,0,0)):
        click(596,386)
        # sleep(0.01)
    if pyautogui.pixelMatchesColor(680,393, (0,0,0)):
        click(680,393)
        # sleep(0.01)
    if pyautogui.pixelMatchesColor(773,390, (0,0,0)):
        click(773,390)
        # sleep(0.01)