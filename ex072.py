"""Crie um programa que tenha uma tupla totalmente preenchida com uma tupla totalmente preenchida por extenso, de zero
até vinte
Seu programa deverá let um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso."""

ext = ("zero", "um", "dois", "três", "quatro",
       "cinco", "seis", "sete", "oito", "nove",
       "dez", "onze", "doze", "treze", "catorze",
       "quinze", "dezesseis", "dezessete", "dezoito",
       "dezenove", "vinte")

while True:
    continua = " "
    num = int(input("Digite um número entre 0 e 20: ").strip())
    if num <= 20 and num >= 0:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o número {ext[num]}")


