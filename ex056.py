"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

* A média de idade do grupo
* Qual é o nome do homem mais velho
* Quantas mulheres têm menos de 20 anos."""

soma_idade = 0
media_idade = 0
maioridade_homem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo? [M/F]: ').strip())
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade}')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridade_homem} anos' )
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
