'''
Crie um programa onde o usuario possa digitar varios valores numericos 
e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao
sera adicionado. No final, serao exibidos os valores unicos digitados,
em ordem crescente.
'''

numero = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numero: #Se nao existe o valor n em numeros
        numero.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-'*30)
numero.sort()
print(f'Voce digitou os valores {numero}')
