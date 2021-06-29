"""Faça um programa que jogue par ou impar com o computador.O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo."""

from random import randint, choice
print('=-' * 10)
print('JOGO DE PAR OU IMPAR')
print('=-' * 10)

vitorias = 0
while True:
    valor = int(input('Digite um valor: ').strip())
    pi = str(input('Par ou Impar? [P/I]: ').strip().upper())[0]
    pc = randint(0, 10)
    pipc = choice(['P', 'I'])
    soma = valor + pc
    calculo = soma % 2
    if calculo == 0 and pi == 'I':
        print(f'Você jogou {valor} e o PC {pc}.Total de {soma}, DEU PAR')
        print('VOCÊ PERDEU')
        break
    elif calculo == 1 and pi == 'P':
        print(f'Você jogou {valor} e o PC {pc}.Total de {soma}, DEU IMPAR')
        print('VOCÊ PERDEU')
        break
    elif calculo == 0 and pi == 'P':
        vitorias += 1
        print('VOCÊ VENCEU, VAMOS DE NOVO...')
    elif calculo == 1 and pi == 'I':
        vitorias += 1
        print('VOCÊ VENCEU, VAMOS DE NOVO...')
print(f'Total de vitórias, {vitorias}')

