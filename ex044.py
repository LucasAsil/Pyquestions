"""Elabore um programa que calcule o valor a ser pago por um produto conssiderando
o seu preço normal e condição de pagamento:

- á vista dinheiro no cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

preco = float(input('Quanto custa o produto que deseja comprar?: R$').strip())
print("""Formas de pagamentos:
[ 1 ] á vista dinheiro/cheque: 10% de desconto
[ 2 ] á vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros""")
opcao = int(input('Qual a forma de pagamento?: '))

if opcao == 1:
    print(f'A vista no dinheiro tem desconto de 10%, custava R${preco}, agora custa R${preco - (preco * 10 / 100):.2f}')
elif opcao == 2:
    print(f'A vista no cartão tem desconto de 5%, custava R${preco}, agora custa R${preco - (preco * 5 / 100):.2f}')
elif opcao == 3:
    print(f'Em até 2x no cartão fica 2 parcelas de R${preco / 2:.2f} sem juros')

if opcao == 4:
    parcelas = int(input('Em quantas vezes deseja fazer a compra?'))
    total = preco + (preco * 20 / 100)
    print(f'Sua compra será parcelada em {parcelas}x de R${total / parcelas:.2f} com juros')
    print(f'Sua compra que custava {preco} vai custar {total}')
else:
    print('OPÇÃO INVALIDA. TENTE NOVAMENTE')
