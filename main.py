import pyautogui
import time
import pyperclip
import sys
import os
import subprocess

#Responsavel por baixar as bibliotecas necessarias automaticamente
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])

if not os.path.exists('PROBLEMAS.txt'):
    with open('PROBLEMAS.txt', 'w', encoding='utf-8') as createProblems:
        createProblems.write('')

if not os.path.exists('SOLUÇÃO.txt'):
    with open('SOLUÇÃO.txt', 'w', encoding='utf-8') as createSolution:
        createSolution.write('')


# Função 'range' serve para determinar de quando a quando voce quer comecar a contagem : range(inicio, fim)
for NumPage in range(4600, 10000):

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
         with open('PROBLEMAS.txt', 'a', encoding='utf-8') as createProblems:
            valueProblem = valueProblem.strip('\n')
            createProblems.write(str(valueProblem))     

    #Seleciona e copia os valores de soluções
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.click(-1007,599)
    pyautogui.hotkey('ctrl', 'c')
    valueSolution = str(pyperclip.paste())

    #Verifica se o valor é nulo e caso falso, seleciona o bloco de notas e salva
    if not 'Solução' in valueSolution :
        with open('SOLUÇÃO.txt', 'a', encoding='utf-8') as createSolutions:
            valueSolution = valueSolution.strip('\n')
            createSolutions.write(str(valueSolution))
    
