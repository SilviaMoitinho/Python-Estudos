'''
Melhore o jogo do desafio 028 onde o computador vai 'pensar' 
em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessarios para vencer
'''

from random import randint
from time import sleep

tentativas = 0
computador = randint(0, 10)

print('\033[35m╔─━━━━━━━━━━━━━━▼✧▼━━━━━━━━━━━━━━─╗\033[m')
print('')
print('Vou pensar em um numero entre \033[33m0 e 10\033[m')
print('Sera que voce consegue adivinhar? ')
print('')
print('\033[35m╚─━━━━━━━━━━━━━━▣◉▣━━━━━━━━━━━━━━─╝\033[m')
sleep(3)

for c in range (3, 0, -1):
    print(c)
    sleep(0.5)

jogador = int(input('Faça o seu palpite -> '))

while computador != jogador:
    print('Pensando...')
    sleep(1)
    jogador = int(input('Voce... \033[31mERROU\033[m! Tente de novo -> '))
    tentativas += 1

print('Pensando...')
sleep(1)

if tentativas == 0:
    print('\033[34mUAU\033[m! Voce venceu de \033[32mPRIMEIRA\033[m, PARABENS!\n')
    print('Voce desbloqueou a recompensa, \033[32mCOROA DO REI\033[m \n' \
    '↳ ♛')
elif tentativas == 1:
    print('Voce...\033[32mACERTOU\033[m, e precisou apenas de UMA tentaiva, impressionante!\n')
    print('Voce desbloqueou a recompensa, \033[36mFLOR DA VITORIA\033[m\n' \
    '↳ ❁')
else: 
    print('Voce... \033[32mACERTOU\033[m, mas precisou de {} tentivas para acertar!'.format(tentativas))
    print('\033[41mNAO desbloqueou o premio!\033[m')
    