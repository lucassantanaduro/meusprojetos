#https://guitarflash.com/
#Nesse projeto foi usado identificação de cores em determinadas posições na tela

import pyautogui
import keyboard

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(993,727,(255,0,0),tolerance=20):
        pyautogui.press('s')
    if pyautogui.pixelMatchesColor(1081,727,(244,244,0),tolerance=20):
        pyautogui.press('j')
    if pyautogui.pixelMatchesColor(902,728,(0,153,0),tolerance=20):
        pyautogui.press('a')