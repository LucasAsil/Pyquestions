"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

num = int(input('Digite um número inteiro: ').strip())
print("""Escolha a conversão: 
[ 1 ] \033[1;32m Converter em BINÁRIO \033[m
[ 2 ] \033[1;35m Converter em OCTAL \033[m
[ 3 ]  \033[1;34mConverter em HEXADECIMAL \033[m""")
opcao = int(input('Sua opção: ').strip())

if opcao == 1:
    print(f'{num} convertido para \033[1;32m BINÁRIO \033[m é igual a {bin(num) [2:]}')
elif opcao == 2:
    print(f'{num} convertido para \033[1;35m OCTA \033[m é igual a {oct(num) [2:]}')
elif opcao == 3:
    print(f'{num} convertido para \033[1;34m HEXADECIMAL \033[m é igual a {hex(num) [2:]}')
else:
    print('Opção inválida, tente novamente!')
