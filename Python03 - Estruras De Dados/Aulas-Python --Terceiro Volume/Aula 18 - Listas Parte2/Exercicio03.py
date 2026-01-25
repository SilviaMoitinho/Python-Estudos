'''
Crie um programa que crie uma matriz de dimensao 3x3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formataçao correta.
'''

matriz = [[],[],[]]
p = s = 0
for c in range(0,9):
    matriz[p].append(int(input(f'Digite um valor para [{p},{s}]: ')))
    s += 1
    if s == 3:
        p += 1
        s = 0
print('-'*30)
for m in matriz:
    for c in range(0,3):
        print(f'[{m[c]:^5}]', end=' ')
    print()
