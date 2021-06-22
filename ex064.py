"""Crie um programa que leia vários números inteiros pelo teclado.O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)."""
n = cont = soma = 0
n = int(input('Digite um número (999 para parar): ').strip())
while n != 999:
    cont += 1
    soma += n
    n = int(input('Outro número (999 para parar): ').strip())
print('Contagem enecerrada')
print(f'Foram digitados {cont} números.E a soma entre eles foi de {soma}')