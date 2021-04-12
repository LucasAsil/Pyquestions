"""A Confederação nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFATIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""

from datetime import date
#Contém biblioteca de emoji
from emoji import emojize as emo #Denominando 'emo' para emojize.(comando menor)
nascimento = int(input('Qual o nascimento do atleta?: ').strip())
ano = date.today().year
idade = ano - nascimento

print(f'A idade do atleta é: {idade}')
if idade <= 9:
    print('Classificação: Atleta MIRIM', emo(':baby:', use_aliases=True)) #Outro jeito de usar Emojis
elif idade <= 14:
    print('Classificação: Atleta INFANTIL \U0001f466')
elif idade <= 19:
    print('Classificação: Atleta JUNIOR \U0001f468')
elif idade <= 20:
    print('Classificação: Atleta SÊNIOR \U0001f474')
elif idade > 20:
    print('Classificação: Atleta MASTER \U0001f60e')