"""Crie um programa que leia o ano de nascimento de sete pessoas.No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""

from datetime import date

maiores = 0
menores = 0
atual = date.today().year
for c in range(1, 8):
    nascimento = int(input(f'Digite em que ano {c}ª pessoa nasceu: ').strip())
    idade = atual - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} pessoas maiores de idade\nE {menores} pessoas menores de idade.')
