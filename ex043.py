"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40:Obesidade
- Acima de 40: Obesidade mórbida """

peso = float(input('Qual é o seu peso (Kg)?: ').strip())
altura = float(input('Qual é a sua altura (m)?: ').strip())
imc = peso / (altura ** 2)
print(f'O seu IMC: {imc:.1f}')

if imc < 18.5:
    print('Abaixo de 18.5: Abaixo do Peso')
elif 18.5 < imc < 25:
    print('Entre 18.5 e 25: Peso ideal')
elif 25 < imc < 30:
    print('25 até 30: Sobrepeso')
elif 30 < imc < 40:
    print('30 até 40:Obesidade')
elif imc > 40:
    print('Acima de 40: Obesidade mórbida')
