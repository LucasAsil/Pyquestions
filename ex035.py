#Analyzing Triangles
"""Desenvolva um programa que leia o comprimento de três retas e diga ao úsuario
se elas podem ou não formar um triangulo."""

print('Descubra se três retas conseguem formar um triângulo!')

lado_a = float(input('Qual a medida do lado (a)? ').strip())
lado_b = float(input('Qual a medida do lado (b)? ').strip())
lado_c = float(input('Qual a medida do lado (c)? ').strip())

if lado_a + lado_b > lado_c:
    print('É POSSIVEL criar um triangulo com essas medidas')
else:
    print('Não é POSSIVEL criar um trinagulo com essas medidas')