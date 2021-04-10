"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado."""

from time import sleep

valor_casa = float(input('\033[1;33m Qual o valor da casa que deseja comprar?\033[m R$:'))
salario = float(input('\033[1;32m Qual o seu salário?\033[m R$:'))
anos = int(input('\033[1;35m Em quantos anos ira pagar o imóvel?\033[m:'))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30/100

print('Calculando empréstimo...')
sleep(5)
if prestacao <= minimo:
    print('\033[1;32m É possivel fazer um empréstimo!!! \033[m')
else:
    print('\033[1;31m Não é possível fazer um empréstimo! \033[m')
