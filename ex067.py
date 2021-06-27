"""Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada usuário. O prgrama será interrompido quando o npumero solicitado
for negativo"""

#3.0
while True:
    num = int(input('Quer ver a tabuada de qual valor?: ').strip())
    if num < 0:
        break
    print('=-' * 20)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=-' * 20)
print('FIM DO PROGRAMA!')
