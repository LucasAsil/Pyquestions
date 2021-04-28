"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exp: 5! = 5x4x3x2x1 = 120"""

from math import factorial

num = int(input('Digite um número para calcular o fatorial: ').strip())
cont = num
f = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont} ', end='')
    print('x' if cont > 1 else '=', end=' ')
    f *= cont
    cont -= 1
print(f'{f}')

