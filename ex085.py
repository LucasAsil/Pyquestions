"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e impares.No final, mostre os valores pares e impares em ordem crescente."""

lista = [[], [], ]
for p in range(1, 8):
    valor = int(input(f"Digite o {p} valor: ").strip())
    if valor % 2 == 1:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print("=-"*30)
print(f"Os valores impares digitados foram: {sorted(lista[0])}")
print(f"Os valores pares digitados foram: {sorted(lista[1])}")
