"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.No final
mostre uma listagem de preços, organizando os dados em forma tabular."""

lista = ("Lápis", 0.75,
         "Borrha", 0.80,
         "Caneta", 2.00,
         "Apontador", 1.50,
         "Estojo", 11.99,
         "Caderno", 46.00,
         "Lápis de cor", 18.00,
         "Cola", 4.50,
         "Mochila", 85.00)

print("="*40)
print("LISTA DE PREÇOS")
print("="*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    else:
        print(f"R${lista[pos]:.2f}")
print("=" * 40)
