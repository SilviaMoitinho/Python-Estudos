'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os numeros pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
'''

matriz = [[],[],[]]
p = s = somapar = cont = maiorseg = somater = 0
for c in range(0,9):
    matriz[p].append(int(input(f'Digite um valor para a posiçao [{p},{s}]: ')))
    s += 1
    if s == 3:
        p += 1
        s = 0
print('-'*30)
for m in matriz:
    for c in range(0,3):
        print(f'[{m[c]:^5}]', end='')
        if m[c] % 2 == 0:
            somapar += m[c]
        if c == 2:
            somater += m[c]
        if cont == 1:
            if c == 0 or m[c] > maiorseg:
                maiorseg = m[c]
    print()
    cont += 1
print('-'*30)
print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somater}')
print(f'O maior valor da segunda linha é {maiorseg}')