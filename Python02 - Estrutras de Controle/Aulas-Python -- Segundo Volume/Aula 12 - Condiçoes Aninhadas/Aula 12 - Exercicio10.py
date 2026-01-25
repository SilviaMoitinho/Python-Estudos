'''
Crie um programa que faça o computador jogar JOKINPO com voce
'''

import emoji
from random import randint
from time import sleep

print('───────── ❖ ─────────')
print('Vamos jogar \033[31mJ\033[32mO\033[33mK\033[34mE\033[35mN\033[36mP\033[31mO\033[m')
print('───────── ❖ ─────────')
print('Escolha...')
sleep(1)
print(emoji.emojize('Pedra :oncoming_fist:'))
sleep(1)
print(emoji.emojize('Papel :hand_with_fingers_splayed:'))
sleep(1)
print(emoji.emojize('Tesoura :victory_hand:'))
jogador = str(input('-> ')).upper()
computador = randint(1,3)
emoji_jogador = str()
emoji_computador = str()

if computador == 1:
    emoji_computador = str(emoji.emojize(':oncoming_fist:'))
elif computador == 2:
    emoji_computador = str(emoji.emojize(':hand_with_fingers_splayed:'))
elif computador == 3:
    emoji_computador = str(emoji.emojize(':victory_hand:'))

if jogador == 'PEDRA':
    emoji_jogador = str(emoji.emojize(':oncoming_fist:'))
elif jogador == 'PAPEL':
    emoji_jogador = str(emoji.emojize(':hand_with_fingers_splayed:'))
elif jogador == 'TESOURA':
    emoji_jogador = str(emoji.emojize(':victory_hand:'))
print('˖˖˖˖˖˖˖˖˖˖—》 {}  VS  {} 《—˖˖˖˖˖˖˖˖˖˖˖'.format(emoji_computador, emoji_jogador))

if jogador == 'PEDRA' and computador == 1 or jogador == 'PAPEL' and computador == 2 or jogador == 'TESOURA' and computador == 3:
    print('\033[33mEMPATE\033[m')
elif jogador == 'PEDRA' and computador == 3:
    print('Voce \033[32mGANHOU\033[m')
elif jogador == 'PEDRA' and computador == 2:
    print('VOCE \033[31mPERDEU\033[m')
elif jogador == 'PAPEL' and computador == 1:
    print('Voce \033[32mGANHOU\033[m')
elif jogador == 'PAPEL' and computador == 3:
    print('Voce \033[31mPERDEU\033[m')
elif jogador == 'TESOURA' and computador == 2:
    print('Voce \033[32mGANHOU\033[m')
elif jogador == 'TESOURA' and computador == 1:
    print('Voce \033[31mPERDEU\033[m')
print('✦ ˚ * ✦ * ˚ ✦ FIM DE JOGO ✦ ˚ * ✦ * ˚ ✦')