'''
Faça um programa que leia um numero qualquer e mostre o seu fatorial
'''

print('   Fatorial com Python')
print('\033[31m•  \033[32m•  \033[33m•  \033[34m•  \033[35m•  \033[36m• \033[31m•  \033[32m•  \033[33m•  \033[34m•  \033[35m•  \033[36m•\033[m ')
print()
print('Digite um numero para calcular o seu fatorial')
n = int(input('-> '))
cont = 1
fatorial = 1

# Utilizando while
if n == 0:
    print('O fatorial de 0 é ZERO')
else:
    while cont != n:
        cont += 1
        fatorial *= cont
print('══════ ••► O fatorial de {} é {}'.format(n, fatorial))

# Utilizando for
for c in range (n, 1, -1):
    cont += 1
    fatorial *= cont
print('══════ ••► O fatorial de {} é {}'.format(n, fatorial))