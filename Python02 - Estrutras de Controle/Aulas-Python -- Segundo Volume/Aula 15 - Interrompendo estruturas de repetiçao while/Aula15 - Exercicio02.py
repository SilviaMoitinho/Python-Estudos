''' 
Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa sera interrompido quando 
o numero solicitado for negativo
'''

print('    Tabuada Python')
print('●❯────────────────❮●')
print('')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = \033[32m{n*c}\033[m')
    print('-'*30)
print('Obrigada por utilizar a tabuada python!')