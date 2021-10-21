""""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint
nums = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),)

# print(f"Os números sorteados são; ", end="")
# for n in nums:
#     print("{n}", end=" ")

# print(f"\nO maior valor sorteado foi; {max(nums)}")
# print(f"O menor valor sorteado foi; {min(nums)}")

#Segundo método
print(f"Os úmeros sorteados são; {nums}")
maior = nums[0]
menor = nums[0]
for m in nums:
    if m > maior:
        maior = m
print(f"O maior é {maior}")
for m in nums:
    if m < menor:
        menor = m
print(f"O menor é {menor}")