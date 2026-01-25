for c in range(1,6): #Vai repetir o que esta dentro do for por 5 vezes
    print('Oi') #      porque quando chega no 6 ele para, ou seja nao considera o ultimo numero
print('FIM')

for c in range(0,6): #Assim ele vai repetir o que esta dentro do for por 6 vezes
    print('oi')
print('fim')

for c in range(1,11): 
    print(c) # Vai mostrar a contagem de 1 ATE 10

for c in range(6,0, -1): # vai contar de 6 ate 1, o ultimo parametro define que recebendo 5 tira menos 1.. e por ai vai
    print(c)
print('Sua contagem regressiva')

for c in range(0,9, 2): # vai contar de 2 em 2, porque colocamos os 2 no ultimo parametro
    print(c)
print('numeros pares')

n = int(input('Digite um numero: '))
for c in range(0, n+1): # Colocamos a variavel input e +1 para que o programa possa ir até aquele limite que a pessoa escolheu,
    print(c) #             pois o programa sempre vai desconsiderar o ultimo numero
print('Fim')

inicio = int(input('Em que numero começa: '))
fim = int(input('Em que numero acaba:'))
passo = int(input('qual a forma? '))
for c in range(inicio, fim+1, passo):
    print(c)
print('final')

s = 0
for c in range(0,3):
    n = int(input('Digite um numero inteiro: ')) # Vai pedir para digitar um numero 3 vezes
    s += n # Para somar os numeros digitados, S recebe S + N (+=)
print('A soma dos numeros é {}'.format(s))