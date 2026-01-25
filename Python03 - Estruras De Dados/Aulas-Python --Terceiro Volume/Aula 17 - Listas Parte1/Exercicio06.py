'''
Crie um programa onde o usuario digite uma expressao qualquer
que use parenteses. Seu aplicativo devera analisar se a expressao
passada esta com os parenteses abertos e fechados respetivamente.
'''

aberto = 0
fechado = 0
exp = input('Digite uma expressao: ')
lista = list(exp)
for c in range(0, len(lista)):
    if lista[c] == '(':
        aberto += 1
    if lista[c] == ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressao esta correta')
else:
    print('Sua expressao esta errada')