import pyautogui
import time
import pyperclip
import sys
import subprocess

#Responsavel por baixar as bibliotecas necessarias automaticamente
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'import pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])

# Função 'range' serve para determinar de quando a quando voce quer comecar a contagem : range(inicio, fim)
for NumPage in range(4355, 10000):

    #Comando pyautogui.position() serve para descobrir a posição do mouse (x e y)
    '''print(pyautogui.position())
    time.sleep(2.5)'''

    #Comando para selecionar a barra de URL e alterar o valor do id, tag responsavel por registrar os chamados por ordem
    pyautogui.moveTo(-1078,63)
    pyautogui.click(-1078,63)
    pyautogui.hotkey('end')
    pyautogui.doubleClick(-976,68)
    time.sleep(0.1)
    pyautogui.typewrite(str(NumPage))
    time.sleep(0.1)
    pyautogui.hotkey('enter')
    time.sleep(0.1)

    #seleciona e copia os o valor de problemas
    pyautogui.click(-1308,599)
    pyautogui.click(-1308,599)
    pyautogui.click(-1308,599)
    pyautogui.hotkey('ctrl', 'c')
    valueProblem = str(pyperclip.paste())

    #Verifica se o valor é nulo e caso falso, seleciona o bloco de notas e salva
    if not '--' in valueProblem:
        pyautogui.click(-362,25)
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 's')
        

    #Seleciona e copia os valores de soluções
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.hotkey('ctrl', 'c')
    valueSolution = str(pyperclip.paste())

    #Verifica se o valor é nulo e caso falso, seleciona o bloco de notas e salva
    if not 'Solução' in valueSolution :
        pyautogui.click(-297,404)
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 's')
    
