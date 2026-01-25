'''
Faça um mini-sistema que utiliza o interactive help do Python.
O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario 
digitar a palavra 'Fim', o programa se encerra.
OBS: Use cores.
'''

from time import(sleep)

c = ('\033[0m', '\033[0;30;41m', '\033[0;30;43m','\033[0;30;44m')

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',3)
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0])
    sleep(1)

#Programa Principal
comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',2)
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo.',1)