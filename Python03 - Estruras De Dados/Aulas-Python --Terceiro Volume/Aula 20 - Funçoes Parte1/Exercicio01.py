'''
Faça um programa que tenha uma funçao chamada area(), que 
receba as dimensoes de um terreno retangular (largura e comprimento)
e mostre a area do terreno.
'''

def area(a,b):
    print(f'A area de um terreno {a}x{b} é de {a*b}m2')


print('  Controle de Terrenos')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)
