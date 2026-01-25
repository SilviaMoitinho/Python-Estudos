'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa,
calcule o seu IMC e mostre seus status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5  e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('Parabens, voce esta na faixa de PESO IDEAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE')
else:
    print('Voce esta em OBESIDADE MORBIDA, cuidado!')