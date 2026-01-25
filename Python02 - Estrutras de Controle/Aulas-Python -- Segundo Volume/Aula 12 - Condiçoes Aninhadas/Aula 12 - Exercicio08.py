'''
Desenvolva uma logica que leia o peso e a altura de uma pessoa,
calcule o seu IMC e mostre seus status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5  e 25: Peso ideal
- 25 ate 30: Sobrepeso
- 30 ate 40: Obesidade
- Acima de 40: Obesidade morbida
'''

from time import sleep

print('\033[36m-\033[m'*100)
print('Calcula o seu IMC (Indice de Massa Corporal) e descubra qual a sua categoria')
print('\033[36m-\033[m'*100)

a = float(input('Qual a sua altura? '))
m = float(input('Quanto voce pesa? '))
imc = m/ (pow(a,2))

print('Calculando o seu IMC...')
sleep(2)
print('IMC -> {:.1f}'.format(imc))
if imc < 18.5:
    print('Status: \033[1;34mAbaixo do peso\033[m')
elif imc >= 18.5 and imc <= 25:
    print('Status: \033[1;32mPeso ideal\033[m')
elif imc > 25 and imc <= 30:
    print('Status: \033[1;33mSobrepeso\033[m')
elif imc > 30 and imc <= 40:
    print('Status:\033[1;31mObesidade\033[m')
else:
    print('Status: \033[1;35mObesidade morbida\033[m')