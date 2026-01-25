'''
Melhore o jogo do desafio 028 onde o computador vai 'pensar' 
em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessariospara vencer
'''

from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0

while not acertou: #Enquanto o acertou nao ficar true
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menps... Tente mais uma vez')
print('Acertou com {} tentaivas. Parabens'.format(palpites))
