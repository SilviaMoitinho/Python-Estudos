'''
Crie um programa que mostre na tela todos os numeros pares que estao 
no intervalo de 1 a 50
'''

num_par = 0
for c in range(2, 51, 2):
    resultado = c % 2
    if resultado == 0:
        print(c)
        num_par += 1
    else:
        print(c)
print('Total de numeros pares: {}'.format(num_par))