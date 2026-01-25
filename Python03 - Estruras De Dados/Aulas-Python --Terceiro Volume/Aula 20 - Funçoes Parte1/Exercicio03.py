'''
Faça um programa que tenha uma funçao chamada contador(), que receba 3 
parametros: inicio, fim e passo e realize a contagem. Seu programa
tem que realizar 3 contagens atraves da funçao criada.
a) de 1 a 10, de 1 em 1:
b) de 10 a 0, de 2 em 2:
c) Uma contagem personalizada
'''

def contador(a,b,c):
    print('-='*30)
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if b < 0:
        b -= 1
    else:
        b += 1
    if a > b and c > 0:
        for c in range(a,b,-c):
            print(f'{c} ', end='')
    elif a > b and c < 0:
        for c in range(a,b,c):
            print(f'{c} ', end='')
    else:
        for c in range(a,b,c):
            print(f'{c} ', end='')
    print()
    print('-='*30)

    
a = 1
b = 10
c = 1
contador(a,b,c)

a = 10
b = 0
c = 2
contador(a,b,c)

print('Agora é a sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)