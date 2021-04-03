#Cost Travel
"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calculeo preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45
para viagens mais longas"""


dviagem = float(input('Qual a distancia da viagem que deseja fazer?').strip())
price_curto = dviagem * 0.50
price_longo = dviagem * 0.45

if dviagem <= 200:
    print('A sua viagem de custara:', 'R$', price_curto)
else:
    print('Sua viagem ultrapssa 200 Km e custara:', 'R$', price_longo)
