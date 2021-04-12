"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também devera mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

atual = date.today().year #Calculo da data
sexo = str(input('Você é \033[1;34m homem \033[m ou \033[1;35m mulher? \033[m').strip().lower())
#Se for MULHER
if sexo == 'mulher':
    print('Este teste é so para \033[1;34m homens \033[m, você não precisa fazer!')
    exit()
elif sexo == 'homem':
    print('\033[1;33m Muito bem, continue... \033[m')
#Comando invalido
else:
    print('\033[1;31m Comando invalido, tente novamente. \033[m')
    exit()
#Se for HOMEM
nascimento = int(input('Qual seu ano de nascimento?').strip())
idade = atual - nascimento

print(f'\033[1;34m Você nasceu em {nascimento} e tem {idade} anos \033[m')
if idade == 18:
    print('\033[1;32mVocê tem 18 anos, está na hora de se alistar!\033[m')
elif idade < 18:
    print(f'\033[4;29mFalta {18 - idade} ano para o seu alistamento\033[4;29m')
    print(f'Será no ano de {(18 - idade) + atual}')
elif idade > 18:
    print(f'\033[1;31m Você ja passou do prazo de alistamento a {idade - 18} anos!!! \033[1;31m')
    print(f'Ja deveria ter se alistado em {atual - (idade - 18)}')
