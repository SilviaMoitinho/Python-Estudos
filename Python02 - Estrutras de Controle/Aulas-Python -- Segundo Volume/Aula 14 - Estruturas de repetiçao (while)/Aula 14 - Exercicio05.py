''' 
Refaça o desafio 051, lendo o primeiro termo de uma PA, mostrando os 10
primeiros termos da progressao usando a estrutura while
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao:'))
decimo = primeiro + (10 - 1)*razao

while primeiro != decimo + razao:
    print('{}'.format(primeiro), end=' -- ')
    primeiro += razao