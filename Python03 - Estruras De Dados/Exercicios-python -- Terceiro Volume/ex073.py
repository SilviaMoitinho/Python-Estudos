'''
Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol (2025),
na ordem de colocaçao. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times ordem alfabetica
d) Em que posiçao esta o time Chapecoense
'''

times = ('Corithians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia',
         'Sao Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atletico-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros sao: {times[0:5]}')
print('-='*15)
print(f'Os 4 ultimos sao: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-='*15)
print(f'O Chapecoense esta {times.index('Chapecoense')+1}° posiçao')
