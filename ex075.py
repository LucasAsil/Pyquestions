"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


nums = (int(input("Digite um valor; ").strip()),
        int(input("Digite um valor; ").strip()),
        int(input("Digite um valor; ").strip()),
        int(input("Digite um valor; ").strip()))
print(f"Você digitou os valores {nums}")
print(f"O valor 9 apareceu {nums.count(9)} vez.")
if 3 in nums:
    print(f"O valor 3 foi digitado na posição {nums.index(3)+1}.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print(f"Os números pares foram; ", end="")
for n in nums:
    if n % 2 == 0:
        print(n, end=", ")
