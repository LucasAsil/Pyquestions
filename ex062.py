"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disse que quer mostrar 0 termos."""

#3.0
print('Gerador de PA')
print('=-=' * 10)
primeiro = int(input('Digite o primeiro termo: ').strip())
razao = int(input('Digite a razão da PA: ').strip())
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print(f'{termo} ->', end=' ')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais'))
print(f'Finalizado com {total} mostrados')
