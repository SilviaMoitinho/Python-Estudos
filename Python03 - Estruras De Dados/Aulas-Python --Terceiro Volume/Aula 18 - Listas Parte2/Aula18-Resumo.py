#Fazendo copias
teste = list()
teste.append('Silvia')
teste.append(26)
galera = list()
galera.append(teste[:]) #Simbolo para fazer a copia
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste[:])
print(galera)

#Declarando listas
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

#Fatiando a lista
print(galera) #Mostra a lista completa
print(galera[0]) #So os dados da primeira pessoa, joao 19
print(galera[0][0]) #So os dados da primeira pessoa, e dentro os dados da posiçao 0: joao
print(galera[2][1]) #Vai mostrar a pessoa na posiçao 2, e dentro os dados da posiçao 1: 13

#Fatiando com for
for p in galera:
    print(p) #Vai mostrar nome e idade de cada um na lista
    print(p[0]) #Vai mostrar apenas os nomes
    print(p[1]) #Vai mostrar apenas a idade
    print(f'{p[0]} tem {p[1]} anos de idade.') #Print formatado, vai mostrar os 2 de cada pessoa na lista (nome e idade)

#Preenchendo com INPUT
galera = list()
dados = list()
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('Nome: '))) #Colocamos o nome da pessoa dentro da lista dados
    dados.append(int(input('Idade: '))) #E a idade tambem
    galera.append(dados[:]) #Copiamos a lista dados para a lista galera
    dados.clear() #Excluimos os dados dentro da lista dados, para ficar vazia

#Procurando dados dentro da lista
for p in galera:
    if p[1] >= 21: #Se em cada p[1](idade)
        print(f'{p[0]} é maior de idade') #P[0](nome)
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')