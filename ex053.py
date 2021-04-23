"""Crie um programa que leia uma frase qualquer e diga se ela é um palindromo,
desconsiderando os espaços"""

frase = str(input('Digite uma frase: ').strip()).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')

