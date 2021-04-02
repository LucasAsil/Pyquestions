#Guess Number!
"""Escreva um programa que faça o computador 'pensar' em um numero inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador.

O programa deverá escrever na tela se o usúario acertou ou errou"""

#v1.0
import random

print('O computador ira escolher um número aleatório qualquer entre 0 e 5, tente adivinhar...')

ncomp = random.randint(1,5)
nuser = int(input('Vamos lá...Qual é o numero escolhido pelo computador?'))


if nuser == ncomp:
    print('VOCÊ ACERTOU, PARABÉNS!')
else:
    print('VOCÊ ERROU, TENTE NOVAMENTE')
