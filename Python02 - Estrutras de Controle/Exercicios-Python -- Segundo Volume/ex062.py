''' 
Melhore o desafio 061 , perguntando para o usuario se 
ele quer que mostre mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos
'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao de PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais'))
print('Progressao finalizada com {} termos mostrados'.format(total))
