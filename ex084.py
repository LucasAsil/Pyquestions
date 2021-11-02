"""Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoa = []
dado = []
mai = men = 0
while True:
    dado.append(str(input("Nome: ").strip()))
    dado.append(int(input("Peso: ").strip()))
    if len(pessoa) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    R = str(input("Continuar? [S/N]: ").strip().upper())
    if R in "N":
        break
print(f"{len(pessoa)} pessoas foram cadastradas.")
print(f"O maior peso foi de {mai}Kg. Peso de ", end="")
for p in pessoa:
    if p[1] == mai:
        print(f"{p[0]}", end=", ")
print()
print(f"O menor peso foi de {men}Kg. Peso de ", end="")
for p in pessoa:
    if p[1] == men:
        print(f"{p[0]}", end=", ")
