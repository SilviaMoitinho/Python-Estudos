'''
Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artificio, indo de 10 a 0, com uma
pausa de 1 segundo entre eles.
'''

from time import sleep
import emoji
from datetime import date, datetime

hoje = datetime.today().year
print('*: ･ ﾟ ✧ \033[32m Contagem Regressiva para\033[m {} '.format(hoje + 1))
for c in range(10, -1, -1):
    sleep(1)
    if c == 0:
        c = emoji.emojize(':fireworks:' ':fireworks:' ':fireworks:')
    print(c)
print('\033[36m*: ･ ﾟ ✧ * \033[33mFeliz Ano Novo!\033[m \033[36m*: ･ ﾟ ✧ *\033[m')
print('{:･^40}'.format(' 2026 '))