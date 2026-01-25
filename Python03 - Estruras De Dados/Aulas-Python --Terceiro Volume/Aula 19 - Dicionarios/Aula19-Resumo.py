#Declarando dicionario de forma simples
pessoas = {'nome':'Guanabara', 'sexo': 'M', 'idade':22}
print(pessoas[0]) #Da erro, o elemento 0 é o nome
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #Como o print formatado tem aspas, quando for colocar dentro de {} usar aspas duplas
print(pessoas.keys()) #Vai mostrar as chaves - Nome, sexo e idade
print(pessoas.values()) #Vai mostrar os valores - Guanabara, M, 22
print(pessoas.items()) #Mostra os dois (valores e chaves)

#Apagando elementos
del pessoas['sexo']

#Mudando os valores
pessoas['nome'] = 'Silvia'

#Adicionando elementos
pessoas['peso'] = 60

#Para referenciar os elemntos usamos [], para declarar usamos {}

#Acessar chaves, valores e itens por laços
for k in pessoas.keys():
    print(k) # Vai mostrar todas as chaves
for v in pessoas.values():
    print(v) #Vai mostrar todos os valores
for k,v in pessoas.items():
    print(f'{k} = {v}') #Mostra a chave(k) os valores(v) nos items

#Criar um dicionario dentro de uma lista
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'Sao Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]) #O elemento 0 - estado1
print(brasil[1]) #estado2
print(brasil[0]['uf']) #Elemento 0, dicionario estado1 elemento 'uf' - Rio de Janeiro
print(brasil[1]['sigla']) #SP

#Colocando elementos em dicionarios com laços e input
estado = dict()
brasil = list()
for c in range(0,3): #Alimentando a lista e dicionario
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #Temos de usar o copy, para copiar o que esta dentro do dicionario para a lista
for e in brasil: #Mostrando a lista 
    print(e) #Para cada estado do brasil, ele mostra o estado
    for k,v in e.items(): #Mostrando o dicionario
        print(f'O campo {k} tem o valor {v}.')
    for v in e.values():#Mostrando os valores do dicionario
      print(v, end=' ')
    print()