c = 1
while c < 10: # Enquanto o c for menor que 10 faça
    print(c)  # isso equivale ao for c in range(1, 10):
    c += 1
print('Fim')

''' 
O for e o while servem para todas as situaçoes onde nos sabemos o limite
mas quando nao sabemos o limite, o for ja nao é util. Para isso melhor usar o while
'''

n = 1
while n != 0:  # Enquanto o numero for diferente de 0 o programa nao ia parar
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S': # Enquanto a resposta for sim o programa nao para
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

n = 1
par = impar = 0 # Assim as duas variantes recebem 0
while n != 0: # Enquanto o n for diferente de 0 o programa vai ler os numeros digitador
    n = int(input('Digite um valor: '))
    if n != 0: # Como o programa quando chegar no 0, o 0 tambem iria aparecer como numero par, para isso nao acontecer, colocamos esse if
        if n % 2 == 0: # E vai fazer a soma de quantos sao pares e de quantos sao impares
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares, e {} numeros impares'.format(par, impar))
