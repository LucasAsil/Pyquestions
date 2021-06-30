"""Crie um programa que leia o nome e o preço de vários produtos.O programa
vai continuar.No final, mostre:
A) Qual é o total de gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato."""

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o produto: ').strip())
    preco = float(input('Digite o preço: R$').strip())
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]?').strip()).upper()[0]
    if continua == 'N':
        break
print('FIM DO PROGRAMA!')
print(f'O total da compra deu R${total:.2f}')
print(f'{totmil} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {barato} de R${menor} reais.')
