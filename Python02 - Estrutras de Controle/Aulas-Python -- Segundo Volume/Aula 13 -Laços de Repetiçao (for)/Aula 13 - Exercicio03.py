'''
Faça um programa que calcule a soma entre todos os numeros impares que sao 
multiplos de 3 e que encontram no intervalo de 1 até 500
'''
soma = 0
for c in range (1, 501, 2):
    resultado = c % 3
    if resultado == 0:
        soma += c
        print(c)
print('A soma de todos os numeros multiplos de 3 é {}'.format(soma))