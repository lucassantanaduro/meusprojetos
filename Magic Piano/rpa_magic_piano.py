#https://gameforge.com/en-US/littlegames/magic-piano-tiles/?_gl=1*1tmgxvw*_ga*MjU2NTcxMDQuMTczODY5Nzk1NQ..*_ga_37GXT4VGQK*MTc0MTA4OTYwMS44NC4xLjE3NDEwODk2NDUuMC4wLjA.
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

#Foi necessario fazer o click dessa forma porque a biblioteca pyautogui
#nao correspondeu tão bem a velocidade do cursor quanto a biblioteca win32
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(997,341,(0,0,0),tolerance=20):
        click(997,341)
    if pyautogui.pixelMatchesColor(1064,341,(0,0,0),tolerance=20):
        click(1064,341)
    if pyautogui.pixelMatchesColor(1132,341,(0,0,0),tolerance=20):
        click(1132,341)
    if pyautogui.pixelMatchesColor(1200,341,(0,0,0),tolerance=20):
        click(1200,341)
