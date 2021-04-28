"""Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Trocar números
[5] Sair do programa

Seu programa devera realizar as operações solicitadas em cada caso. """
from time import sleep

n1 = int(input('Digite o primeiro número: ').strip())
n2 = int(input('Digite o segundo número: ').strip())
opcao = 0
while opcao != 5:
    print("""\033[34mOque você deseja fazer: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Trocar números
    [5] Sair do programa\033[m""")
    escolha = int(input('Escolher: ').strip())
    if escolha == 1:
        soma = n1 + n2
        print(f'\033[32mResultado de {n1} + {n2} = {soma}\033[m')
    elif escolha == 2:
        vezes = n1 * n2
        print(f'\033[32mResultado de {n1} * {n2} = {vezes}\033[m')
    elif escolha == 3:
        if n1 > n2:
            print(f'\033[32m{n1} é maior que {n2}\033[m')
        else:
            print(f'\033[32m{n2} é maior que {n1}\033[m')
    elif escolha == 4:
        print('\033[1:33mInforme os números novamente:\033[m')
        n1 = int(input('Digite o primeiro número: ').strip())
        n2 = int(input('Digite o segundo número: ').strip())
    elif escolha == 5:
        opcao = 5
        print('\033[1:33mFinalizando...\033[m')
    else:
        opcao = 5
        print('\033[1:31mValor inválido, tente novamente!\033[m')
    sleep(3)
    print('=-=' * 10)
print('Fim')
