"""Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é
maior
- O segundo valor é
maior
-Não existe valor maior, os dois são
iguais"""

valor1 = int(input('\033[1;33m Digite o primeiro valor: \033[m').strip())
valor2 = int(input('\033[1;34m Digite o segundo valor: \033[m').strip())

if valor1 > valor2:
    print(f'O PRIMEIRO valor é maior que o segundo!')
elif valor2 > valor1:
    print('O SEGUNDO valor é maior que o primeiro!')
else:
    print('\033[4;35mNão existe valor maior, os dois são iguais!\033[m')
