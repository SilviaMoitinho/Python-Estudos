'''
Crie um programa que leia nome e duas notas de varios alunos
e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a media de cada um e permita que o usuario possa
mostrar as notas de cada aluno individualmente
'''

listaGeral = [[]]
cont = 0
while True:
    listaGeral[cont].append(str(input('Nome: ')).capitalize())
    listaGeral[cont].append(float(input('Nota 1: ')))
    listaGeral[cont].append(float(input('Nota 2: ')))
    media = (listaGeral[cont][1] + listaGeral[cont][2])/2
    listaGeral[cont].append([media])
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    listaGeral.append([])
print('-'*30)
print('{:<5}'.format('N°.'), end='')
print('{:^10}'.format('Nome'), end='')
print('{:>10}'.format('Media'))
for c in range(0, len(listaGeral)):
    print('{:<5}'.format(f'{c}'), end='')
    print('{:<10}'.format(f'{listaGeral[c][0]}'),end='')
    print('{:>10}'.format(f'{listaGeral[c][3]}'))
while True:
    resp = int(input('Mostrar as notas de qual aluno? (999 para parar) '))
    if resp == 999:
        break
    if resp <= len(listaGeral):
        print(f'Notas de {listaGeral[resp][0]}. Nota 1: {listaGeral[resp][1]} Nota 2: {listaGeral[resp][2]}')
print('{:-^30}'.format(' Volte Sempre '))
