#Multiple Increases
"""Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual é o salário do funcionário?').strip())

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'Quem ganhava R${salario:.2f} antes, agora fica: R${novo:.2f}')
else:
    novo = salario + (salario * 10 / 100)
    print(f'Quem ganhava R${salario:.2f} antes, agora fica: R${novo:.2f}')
