"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores impares digitados respectivamente.
Ao final mostre o conteúdo das três listas geradas."""

fullList = []
oddList = []
pairList = []
while True:
    num = int(input("Digite um número: ").strip())
    R = str(input("Quer continuar [S/N]?: ").strip().upper())
    if R in "N":
        break
    fullList.append(num)
    if num % 2 == 1:
        oddList.append(num)
    elif num % 2 == 0:
        pairList.append(num)

print(f"A lista completa é {fullList}")
print(f"A lista de números pares é {pairList}")
print(f"A lista de números impares é {oddList}")