#https://www.crazygames.com/game/doge-miner-2
#Zerando o jogo Doge Miner 2

import pyautogui
from time import sleep
pyautogui.moveTo(1105,334, duration=2)
for i in range(1,5000) :
    pyautogui.click()
    print(f'click nº{i}')