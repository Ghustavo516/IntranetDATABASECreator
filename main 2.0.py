import pyautogui
import time
import pyperclip

for NumPage in range(4355, 10000):
    '''print(pyautogui.position())
    time.sleep(2.5)'''

    pyautogui.moveTo(-1078,63)
    pyautogui.click(-1078,63)
    pyautogui.hotkey('end')
    pyautogui.doubleClick(-976,68)
    time.sleep(0.1)
    pyautogui.typewrite(str(NumPage))
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(0.1)

    #seleciona e copia os problemas
    pyautogui.click(-1308,599)
    pyautogui.click(-1308,599)
    pyautogui.click(-1308,599)
    pyautogui.hotkey('ctrl', 'c')
    valueProblem = str(pyperclip.paste())

    if not '--' in valueProblem:
        pyautogui.click(-362,25)
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 's')
        #pyautogui.hotkey('enter')

    #seleciona e copia as soluções
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.hotkey('ctrl', 'c')
    valueSolution = str(pyperclip.paste())

    if not 'Solução' in valueSolution :
        pyautogui.click(-297,404)
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 's')
    
    #pyautogui.hotkey('enter')'''
