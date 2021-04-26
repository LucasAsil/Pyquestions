"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'.Caso esteja errado, peça a digitação novamente até ter um valor correto."""
m = 'M'
f = 'F'
while m == 'M' and f == 'F':
    s = str(input('Qual o seu sexo [M/F]: ').strip()).upper()
    if s != 'M' and s != 'F':
        print('\033[1:31mComando invalido, tente novamente!\033[m')
    else:
        print('FIM')

