"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import choice

print('\033[1;35m Vamos jogar JOKENPÔ! \033[m')
print('Escolha entre PEDRA, PAPEL e TESOURA: ')

lista = ['pedra', 'papel', 'tesoura']
#Variaveis PLAYER
escolha_player = str(input('Escolher: ').strip().lower())

#Variaveis PC
escolha_pc = choice(lista)

print(f'\033[1;34mPC:\033[m Eu escolhi {escolha_pc}')
#EMPATE
if escolha_player == escolha_pc:
    print('\033[1;33m Deu empate, tente novamente \033[1;33m')
#Jogador GANHA:
elif escolha_player == 'pedra' and escolha_pc == 'tesoura':
    print('\033[1;34m Droga, você ganhou.Vamos de novo? \033[m')
elif escolha_player == 'papel' and escolha_pc == 'pedra':
    print('\033[1;34m Droga, você ganhou.Vamos de novo? \033[m')
elif escolha_player == 'tesoura' and escolha_pc == 'papel':
    print('\033[1;34m Droga, você ganhou.Vamos de novo? \033[m')
#Jogador PERDE:
elif escolha_pc == 'pedra' and escolha_player == 'tesoura':
    print('\033[1;31m Você perdeu, tente de novo \033[m')
elif escolha_pc == 'pepel' and escolha_player == 'pedra':
    print('\033[1;31m Você perdeu, tente de novo \033[m')
elif escolha_pc == 'tesoura' and escolha_player == 'papel':
    print('\033[1;31m Você perdeu, tente de novo \033[m')
