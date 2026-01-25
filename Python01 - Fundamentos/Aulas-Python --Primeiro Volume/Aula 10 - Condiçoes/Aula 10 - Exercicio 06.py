'''
Faça um programa que leia 3 numeros e mostre 
qual é o maior e qual é o menor
'''

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
print('Analisando os seus numeros...')

if n1 > n2 and n1 > n3:
    print('O maior numero é {}'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O maior numero é {}'.format(n2))
    else:
        print('O maior numero é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor numero é {}'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O menor numero é {}'.format(n2))
    else:
        print('O menor numero é {}'.format(n3))