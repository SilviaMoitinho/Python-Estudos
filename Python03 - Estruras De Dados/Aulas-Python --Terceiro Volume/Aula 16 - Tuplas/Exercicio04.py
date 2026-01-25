'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes aparece o valor 9
b) Em que posiçao foi digitado o primeiro valor 3
c) Quais foram os numeros pares
'''
tu = (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))
if tu.count(9) == 0:
    print('Nao existe o valor 9 nos numeros indicados')
elif tu.count(9) == 1:
    print(f'O numero 9 aparece {tu.count(9)} vez')
else:
    print(f'O numero 9 aparece {tu.count(9)} vezes')
print('')
if tu.count(3) == 0:
    print('Nao existe o valor 3 nos numeros indicados')
else:
    print(f'O valor 3 foi digitado pela primeira vez na {tu.index(3)+1}° posiçao')
print('O numeros pares sao: ', end='')
for c in range (0,4):
    if tu[c] % 2 == 0:
        print(f'{tu[c]}', end=' ')
    