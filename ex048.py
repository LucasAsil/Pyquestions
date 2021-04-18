"""Faça um programa que calcule a soma entre todos os números impares que são
multiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0
cont = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        cont += 1
        soma += impares
print(f'A soma de todos os {cont} valores é {soma}')