"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileirao de Futebol, na ordem de
colocação.Depois mostre:

A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense"""

times = ("Atlético-MG", "Flamengo", "Bragantino", "Palmeiras", "Fortaleza",
         "Corinthians", "Internacional", "Athletico-PR", "Fluminense", "América-MG",
         "Atlético-GO", "Cuiabá", "São Paulo", "Ceará", "Juventude",
         "Santos", "Bahia", "Sport", "Grêmio", "Chapecoense",)

print("=-"*20)
print(f"Lista de times do Brasileirão; {times}.")
print("=-"*20)
print(f"Os 5 primeiros times; {times[:5]}.")  # A
print("=-"*20)
print(f"Os ultimos 4 colocados são; {times[-4:]}.")  # B
print("=-"*20)
print(f"Os times em ordem alfabética; {sorted(times)}.")   # C
print("=-"*20)
print(f"O Chapecoense esta na {times.index('Chapecoense')+1}ª  posição.")   # D

