'''
Refaça o desafio 009 mostrando a tabuada de um numero
que o usuario escolher, so que agora utilizando um laço for
'''

print('          Calcule a tuabada \033[32mGRATIS\033[m')
print('╰─────────────────────✧──────────────────────╮')
n = int(input('Qual numero voce quer ver a tabuada? '))
f = int(input('Ate quanto? '))
for c in range (1, f+1):
    print('{}  \033[31m x \033[m  {} =  {}'.format(n, c, c*n))