'''
Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicionario e todos os
dicionarios em uma lista. No final, mostre:
a) Quantas pessoas foram cadatradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres 
d) Uma lista com todas as pessoas com idade acima da media
'''

di = {}
pessoas = []
mulheres = []
soma_idades = media = 0
while True:
    di['nome'] = str(input('Nome: ')).capitalize()
    di['sexo'] = str(input('Sexo [F/M]: ')).upper().split()[0]
    if di['sexo'] == 'F':
        mulheres.append(di['nome'])
    di['idade'] = int(input('Idade: '))
    soma_idades += di['idade']
    pessoas.append(di.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resp in 'N':
        break
    print(pessoas)
print('-'*30)
print(f'O grupo tem {len(pessoas)} pessoas')
media = soma_idades/len(pessoas)
print(f'A media da idade do grupo é {media:.1f}')
print('As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(f'{m} ', end='')
print('\nLista das pessoas que estao acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(pessoas[c])