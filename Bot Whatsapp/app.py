import webbrowser
import pyautogui
import pyperclip
from time import sleep

telefones = []

def mensagem_com_caracteres_especiais(mensagem):
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl','v')

with open('telefones.txt','r') as arquivo:
    for telefone in arquivo:
        telefones.append(telefone)

print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(730,361,duration=1)
    sleep(2)
    pyautogui.click(794,226,duration=1)
    sleep(6)
    mensagem_com_caracteres_especiais('Essa mensagem é fruto de uma automação')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)