"""Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com a média
atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERÇÃO

- Média 7.0 ou superior:
APROVADO"""

nota1 = float(input('Digite a primeira nota: ').strip())
nota2 = float(input('Digite a segunda nota: ').strip())
media = (nota1 + nota2) / 2
print(f'Com nota {nota1} e {nota2}, a média e {media}')

if media < 5:
    print('\033[1;31m REPROVADO \033[m')
elif media > 5 and media < 6.9:
    print('\033[1;33m RECUPERAÇÃO \033[m')
elif media > 7.0:
    print('\033[1;32m APROVADO! \033[m')
