'''
Crie um programa onde o usuario possa digitar 5 valores numericos
e cadastre-os em uma lista, ja na posiçao correta de inserçao, (sem usar o sort)
No final, mostre a lista ordenada na tela. 
'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #Lista[-1] para descobrir o ultimo elemento
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista...')
                break
            pos += 1
print('-'*30)
print(f'Os valores digitados foram {lista}')
