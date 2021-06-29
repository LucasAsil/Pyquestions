"""Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos"""

tot18 = homem = totm20 = 0
while True:
    print('=' * 20)
    print('CADASTRO DE PESSOA')
    print('=' * 20)
    idade = int(input('Idade: ').strip())
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ').strip()).upper()[0]

    if idade > 18:
        tot18 += 1
    if sexo == 'M':
            homem += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]? ').strip()).upper()[0]
    if continua == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de PESSOAS com mais de 18 anos: {tot18}')
print(f'Total de HOMENS cadastrados: {homem}')
print(f'Total de MULHERES com menos de 20 anos: {totm20}')