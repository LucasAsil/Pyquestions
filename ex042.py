"""Refaça o EXERCICIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: todos os lados são iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes"""

lado1 = float(input('Digite o primeiro valor: ').strip())
lado2 = float(input('Digite o segundo valor: ').strip())
lado3 = float(input('Digite o terceiro valor: ').strip())
#Conferindo possiblidade de formar TRIÂNGULO
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('É possivel formar um triângulo com os seguimentos acima')
    if lado1 == lado2 == lado3:
        print('Todos os lados são iguais, é um triângulo EQUILÁTERO')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Todos os lados são diferentes, é um triângulo Escaleno')
    else:
        print('Apenas dois lados são iguais, é um triângulo ISÓSCELES')
else:
    print('Não é possivel formar um triângulo com os seguimentos acima')
