"""Crie um programa que leia vários números inteiros pelo teclado.O prorama
só vai parar quando o usuário digitar o valo 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)"""

cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: ').strip())
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números, e a soma entre eles deu {soma}!')
print('FIM')