"""Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre
0 e 10.Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer."""

#v2.0
from random import randint
from time import sleep
print('-=-' * 25)
print('\033[1:35mO computador ira escolher um número de 0 a 10, e você tera de adivinhar!\033[m')
print('-=-' * 25)
print('(\033[1:33mComputador escolhendo...\033[m)\033[m')
sleep(3)
ncomp = randint(0, 10)
nuser = 11
cont = 0
while nuser != ncomp:
    nuser = int(input('Escolha um número: ').strip())
    if nuser == ncomp:
        print('\033[1:32mPARABÉNS, VOCÊ ACERTOU!\033[m')
    else:
        print('\033[1:31mVocê errou, tente novamente\033[m')
        cont += 1
        if nuser > 10 or nuser < 0:
            print('\033[1:31mEsse valor está fora do padrão\033[m')
print(f'\033[1:33mVocê deu {cont} palpites até vencer!\033[m')

