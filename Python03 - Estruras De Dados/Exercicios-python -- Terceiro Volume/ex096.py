'''
Faça um programa que tenha uma funçao chamada area(), que 
receba as dimensoes de um terreno retangular (largura e comprimento)
e mostre a area do terreno.
'''

def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg}x{comp} é de {a}m2.')


print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)