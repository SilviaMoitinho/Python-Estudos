'''
Faça um programa que jogue par ou impar com o computador.
O jogo sera interrompido quando o jogador perder, mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo
'''
from random import randint

par = impar = False
s = vitorias = 0

print('┏━━━━━━━━━━ • ✿ • ━━━━━━━━━━┓')
print('')
print('    Vamos jogar par ou impar? ')
print('')
print('┗━━━━━━━━━━ • ✿ • ━━━━━━━━━━┛')
print('')

while True:
    computador = randint(0,10)
    jogador = int(input('Escolha um numero: '))
    s = jogador + computador
    escolha = str(input('Par ou impar? ')).upper().strip()[0]
    if s % 2 == 0:
        par = True
        print(f'Voce escolheu {jogador} e o computador escolheu {computador} no total é {s}. Deu PAR')
    elif s % 2 == 1:
        impar = True
        print(f'Voce escolheu {jogador} e o computador escolheu {computador} no total é {s}. Deu IMPAR')
    if escolha == 'P' and par == True or escolha == 'I' and impar == True:
        print('\033[1;32mVoce ganhou!\033[m \n Vamos jogar mais uma vez...')
    else:
        print('\033[31mVoce perdeu!\033[m')
        break
    print('-'*50)
    s = 0
    par = impar = False
    vitorias += 1
print('════════'*10)
if vitorias == 0:
    print('Voce nao conseguiu acertar nenhuma. Tente novamente!')
elif vitorias == 1:
    print(f'Voce conseguiu vencer 1 vez! Parabens')
else:
    print(f'Voce conseguir vencer {vitorias} vezes. Parabens!')