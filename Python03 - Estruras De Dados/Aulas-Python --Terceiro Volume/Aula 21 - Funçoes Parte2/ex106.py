'''
Faça um mini-sistema que utiliza o interactive help do Python.
O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario 
digitar a palavra 'Fim', o programa se encerra.
OBS: Use cores.
'''

def sistema():
    while True:
        print('\033[33m-'*30)
        print('   SISTEMA DE AJUDA PyHelp')
        print('-'*30)
        f = str(input('\033[mFunçao ou biblioteca: ')).lower()
        if f == 'fim':
            print('\033[31mObrigada por utilizar nosso sistema\033[m')
            break
        print('\033[32m-='*20)
        print(f'  Acessando o manual do comando {f}')
        print('-='*20)
        print(f'\033[36m',help(f))


sistema()