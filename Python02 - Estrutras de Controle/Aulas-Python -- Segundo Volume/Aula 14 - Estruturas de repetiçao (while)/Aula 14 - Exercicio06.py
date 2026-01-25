''' 
Melhore o desafio 061 , perguntando para o usuario se 
ele quer que mostre mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiro + (10 -1)*razao


while primeiro != decimo + razao:
    print('╰┈➤ {}'.format(primeiro), end=' -- ')
    primeiro += razao

print('')
pergunta = int(input('Quantos termos voce quer ver mais? \n'))
termos = primeiro + (pergunta -1)*razao

while pergunta != 0:
    while primeiro != termos + razao:
        print('╰┈➤ {}'.format(primeiro), end=' -- ')
        primeiro += razao
    print('')
    pergunta = int(input('Quantos termos voce quer ver mais? \n'))
print('━━━━━━━━━━━━━━━ • ✿ • ━━━━━━━━━━━━')
print('Obrigada por utilizar nosso site!')