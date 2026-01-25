'''
Desenvolva um programa que leia 6 numeros inteiros
e mostre a soma daqueles que forem par. Se o valor 
for impar, desconsidere-o.
'''
cont_par = 0
soma = 0
for c in range(1,7):
    print('Digite o {}° numero'.format(c),end='')
    n = int(input('->'))
    resultado = n % 2
    if resultado == 0:
        soma += n
        cont_par += 1
print('Numero total de pares: {}, A soma entre eles é de {}'.format(cont_par, soma))