#Bibliotecas
from random import choice #Escolha de algum valor de uma lista 'choice'
from time import sleep #Temporizador 'sleep'

#Lista
validos = [0, 1, 2, 3]

#Variáveis
contador_user = 0 #Contagem de quantas vezes o usuário acertou
contador_comp = 0 #Contagem de quantas vezes o computador acertou

print('==' * 23)
print("\t   BEM-VINDO(A) AO JOKENPÔ\nPara parar o programa inserir '0 ' na escolha")
print('==' * 23)
sleep(1.5)

print('COMPUTADOR: VOCÊ NÃO VAI GANHAR DE MIM!!! HAHAHA')
sleep(1.5)
while True:
    #Valores disponíveis para o computador
    computador = ['PEDRA', 'PAPEL', 'TESOURA']
    #Escolha do cumputador 
    escolhacomp = choice(computador) 

    #Escolha do usuário
    escolha_user = int(input('O que você vai jogar?\n[1] - PEDRA🪨\n[2] - PAPEL📰\n[3] - TESOURA✂️\nInsira aqui a opção desejada: '))
    #Caso o valor seja inválido será requisitado outro valo até que seja um dos disponíveis (1, 2, 3)
    while escolha_user not in validos:
        sleep(2)
        print('¬' * 5)
        escolha_user = int(input('ESCOLHA INVÁLIDA!\nESCOLHA NOVAMENTE!\n|[1] - PEDRA\n|[2] - PAPEL\n|[3] - TESOURA\nInsira a opção desejada : '))
    #Finalização do programa caso seja digitado '0'
    if escolha_user == 0:
        break

    if escolha_user == 1 and escolhacomp == 'PEDRA':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 🪨 e o computador também jogou 🪨. DEU EMPATE!')
        print('¬' * 10)
        

    elif escolha_user == 1 and escolhacomp == 'PAPEL':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 🪨 e o computador jogou 📰. O COMPUTADOR GANHOU!')
        print('¬' * 10)
        contador_comp += 1

    elif escolha_user == 1 and escolhacomp == 'TESOURA':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 🪨 e o computador jogou ✂️. VOCÊ GANHOU!')
        print('¬' * 10)
        contador_user += 1
    
    elif escolha_user == 2 and escolhacomp == 'PEDRA':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 📰 e o computador jogou 🪨. Você ganhou!')
        print('¬' * 10)
        contador_user += 1
    
    elif escolha_user == 2 and escolhacomp == 'PAPEL':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 📰 e o computador também jogou 📰. DEU EMPATE!')
        print('¬' * 10)

    elif escolha_user == 2 and escolhacomp == 'TESOURA':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou 📰 e o computador jogou ✂️. VOCÊ PERDEU!')
        print('¬' * 10)
        contador_comp += 1

    elif escolha_user == 3 and escolhacomp == 'PEDRA':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou ✂️ e o computador jogou 🪨. VOCÊ PERDEU!')
        print('¬' * 10)
        contador_comp += 1

    elif escolha_user == 3 and escolhacomp == 'PAPEL':
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou ✂️ e o computador jogou 📰. VOCÊ GANHOU!')
        print('¬' * 5)
        contador_user += 1
    
    else:
        print('¬' * 10)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ')
        print('Você jogou ✂️ e o computador também jogou ✂️! DEU EMPATE!')
        print('¬' * 10)

    sleep(1.7)

print('==' * 20)
print('\tFIM DE JOGO')
print(f'Você ganhou {contador_user} vezes.\nE o computador ganhou {contador_comp} vezes')
print('==' * 20)