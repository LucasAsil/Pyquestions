#Smaller and Larger
"""Faça um programa que leia três números e mostre qual é o maior e qual é o
menor."""


n1 = int(input('Primeiro valor: ').strip())
n2 = int(input('Segundo valor: ').strip())
n3 = int(input('Terceiro valor: ').strip())

# Smaller
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor digitado foi: ', menor)


# Larger
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi: ', maior)
