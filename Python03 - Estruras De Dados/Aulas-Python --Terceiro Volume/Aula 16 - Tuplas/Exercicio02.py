'''
Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol (2025),
na ordem de colocaçao. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times ordem alfabetica
d) Em que posiçao esta o time Palmeiras 
'''

times = ('Flamengo','Palmeiras','Cruzeiro','Mirassol','Fluminense','Botafogo','Bahia','Sao Paulo','Gremio','Bragantino','Atletico-MG','Santos','Corinthians','Vasco da Gama','EC Vitoria','Internacional','Ceara SC','Fortaleza','Juventude','Sport Recife')
n = 0
alfabetica = sorted(times)
ti = ''
posiçao = 1

print('{:.^40}'.format('BRASILEIRAO 2025'))
print('━━━━━━━━━━━━━━━━━━//━━━━━━━━━━━━━━━━━━━━')
print('{:^40}'.format('No podio 🏆'))
for c in range (0, len(times)):
    if c == 0 or c < 5:
        n += 1
        print(f'\033[32m{n}°\033[m Colocado -> {times[c]}')
print('')
print('━━━━━━━━━━━━━━━━━━//━━━━━━━━━━━━━━━━━━━━')
print('{:^40}'.format('No Podio da derrota 👎'))
for c in range (len(times), 0, -1):
    if c >= 17:
        print(f'\033[31m{c}°\033[m Posiçao -> {times[c-1]}')
    else:
        break
print('')
print('━━━━━━━━━━━━━━━━━━//━━━━━━━━━━━━━━━━━━━━')
print('Lista de times por ordem alfabetica:')
for c in range(0, len(alfabetica)):
    if c % 2 == 0:
        print(f'\033[32m{alfabetica[c]}\033[m', end=' ')
    else:
        print(f'\033[33m{alfabetica[c]}\033[m', end=' ')
print('')
print('━━━━━━━━━━━━━━━━━━//━━━━━━━━━━━━━━━━━━━━')
for pos, time in enumerate(times):
    ti = times[pos]
    if ti == 'Palmeiras':
        print(f'\n\033[32mPalmeiras\033[m Esta na \033[32m{posiçao}\033[m° posiçao!')
    posiçao += 1