'''
Crie um programa onde o usuario possa digitar 5 valores numericos
e cadastre-os em uma lista, ja na posiçao correta de inserçao, (sem usar o sort)
No final, mostre a lista ordenada na tela. 
'''

v = True
valores = []
valores1 = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        print('Adicionado o PRIMEIRO valor da lista.')
        valores.append(n)
    elif c == 1:
        for c in range(0, len(valores)):
            if n > valores[c]:
                valores.append(n)
                print('Valor adicionado na ultima posiçao')
            else:
                valores.insert(0, n)
                print(f'Valor adicionado na posiçao {c}')
    else:
        for c in range(0, 1):
            if n < valores[c]:
                valores.insert(c, n)
                print(f'Valor adicionado na posiçao {c}')
                break
            if n > valores[c]:
                for c in range(1, len(valores)):
                    if n > valores[c] and len(valores)-1 == c:
                        valores.append(n)
                        print('valor adicionado na ultima posiçao')
                        break
                    if n < valores[c]:
                        valores.insert(c, n)
                        print(f'Valor adicionado na posiçao {c}')
                        break   
print(valores)
