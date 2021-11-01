"""Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

lista = []
while True:
    lista.append(int(input("Digite um valor: ").strip()))
    R = str(input("Quer continuar [S/N]?: ")).strip().upper()
    if R == "N":
        break
print(f"Você digitou {len(lista)} valores.")
lista.sort(reverse=True)
print(f"Os valores em ordem crescente são {lista}")
if 5 not in lista:
    print("O valor 5 não foi encontrado na lista.")
else:
    print("O valor 5 foi encontrado na lista.")
