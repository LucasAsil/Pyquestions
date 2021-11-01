"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.Caso o número ja
exista lá dentro, ele não será adicionado.No final, serão exibidos todos os valores únicos digitados em ordem
crescente."""

lista = []
while True:
    valor = int(input("Digite um valor: ").strip())
    if valor not in lista:
        lista.append(valor)
    else:
        print("Valor ja existe na lista (não adicionado)!")
# Chega se o usuário quer continuar
    R = str(input("Quer continuar [S/N]?: ").strip().upper())
    if R == "N":
        break
    if valor == lista:
        print("Ja existe")
print(f"Os valores digitados foram {sorted(lista)}")
