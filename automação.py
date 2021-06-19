# automação python versão 1.0
# automação para melhorar o desktop

#!---LIVRARIA---#
import pyautogui
import time
#!---CODING---#
pyautogui.alert("Limpador De Temp, não mexa no teclado.")
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write('executar')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('temp')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.press('del')
