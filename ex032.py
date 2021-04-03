#Leap Year
"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""


from datetime import date # Date of actually year
ano = int(input('Qual ano deseja analisar? Coloque 0 para o ano atual:').strip())

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano digitado é bissexto')
else:
    print('O ano não é bissexto')
