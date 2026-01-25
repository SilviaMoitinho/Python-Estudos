'''
Condiçoes Aninhadas (if, elif, else)
'''
nome = str(input('Qual é o seu nome?' ))
if nome == 'Silvia':# So podemos ter um if e podemos ter quantos elif quiser
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Joao' or nome == 'Ana': #ATENçAO colocar or nao and! and = e, or = ou
    print('Seu nome é bem popular no brasil!')
elif nome in 'Claudia Joana Marta': # le-se Se o nome tiver alguma das opçoes entao
    print('Belo nome feminino!')
else:# O else é opcional, podemos colocalo ou nao
    print('Gostei do seu nome.')
print('Prazer em te conhecer, {}. Tenha um bom dia!'.format(nome))