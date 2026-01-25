'''
Aprimore o desafio 093 para que ele funcione com varios jogadores,
incluindo um sistema de visualizaçao de detalhes do aproveitamento 
de cada jogador
'''

jogadores = []
di = {}
gols = [[]]
tot = cont = 0
while True:
    di['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas o {di['nome']} jogou? '))
    for c in range(0, p):
        gols[cont].append(int(input(f'Quantos gols na partida {c}?')))
        tot += gols[cont][c]
    di['gols'] = gols[cont]
    di['total'] = tot
    jogadores.append(di.copy())
    tot = 0
    cont += 1
    resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resp == 'N':
        break
    gols.append([])
print('-='*30)
print(F'{'Co. Nome':<4}{'gols':>10}{'Total':>10}')
print('-'*30)
for c in range(0, len(jogadores)):
    print(f'{c} {jogadores[c]['nome']:<4}', end='')
    print(f'{str(gols[c]):>10}', end='')
    print(f'{jogadores[c]['total']:<10}')
print('-='*30)
while True:
    per = int(input('Mostrar dados de qual jogador? '))
    if per == 999:
        break
    if per > len(jogadores):
        print(f'Erro! Nao existe jogador com codigo {per}! Tente novamente.')
    else:
        print(f'- Levantamento do jogador {jogadores[per]['nome']}')
        for c in range(0, len(gols[c])):
            print(f'No jogo {c} fez {gols[per][c]} gols')
    print('-'*30)