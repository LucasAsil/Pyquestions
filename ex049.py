"""Refaça o desafio 009, mostre a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for."""

#v3.0
num = int(input('Digite um número: ').strip())
for c in range(1, 11):
      print(f'{num} x {c} = {num*c}')