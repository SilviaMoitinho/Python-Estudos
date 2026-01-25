'''
Crie um programa onde o usuario possa digitar varios valores numericos 
e cadastre-os e uma lista. Caso o numero ja exista la dentro, ele nao
sera adicionado. No final, serao exibidos os valores unicos digitados,
em ordem crescente.
'''

from time import sleep
certo = True
contador = []
n = cont = 0
valores = []
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    contador.append(cont)
    if cont == 1:
        print('\033[32mAdicionado com sucesso...\033[m')
        valores.append(n)  
    elif cont != 1:
        for c in range(0, len(valores)):
            if n == valores[c]:
                sleep(1)
                print('\033[31mValor repetido!\033[m Nao vou adicionar...')
                certo = False
                break
    if certo == True and cont !=1:
        print('\033[32mAdicionado com sucesso...\033[m')
        valores.append(n)
    certo = True
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]'))
    if r == 'N':
        break
    sleep(1)
print(f'Voce digitou os valores {sorted(valores)}')
