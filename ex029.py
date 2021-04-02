#Radar
"""Escreva um programa que leia a velocidade de um carro em movimento
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""


vel = int(input('Qual a velocidade do carro?'))
multa = (vel-80)*7

if vel <=80:
    print('Você esta dentro do limite de velocidade, 80Km/h!\n')
else:
    print('Você esta fora do limite de velocidade, sua multa é de:', multa)
