"""Refaça o DESAFIO 51, lendo o primeiro termo e arazão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while."""

#v2.0
print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Digite o primeiro termo: ').strip())
razao = int(input('Digite a razão da PA: ').strip())
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo = termo + razao
    cont += 1
print('FIM')
