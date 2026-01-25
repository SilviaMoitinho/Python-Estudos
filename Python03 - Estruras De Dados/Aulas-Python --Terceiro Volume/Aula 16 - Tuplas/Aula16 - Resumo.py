# No python podemos começar uma variavel composta com 3 maneiras - (tupla) ou {lista} ou [dicionario]

lanche = 'Hamburguer', 'suco', 'pizza', 'pudim' #No puthon3 podemos criar tuplas mesmo sem os ()
print(lanche)
print(lanche[1]) #Suco
print(lanche[-2]) #pizza
print(lanche[1:3]) #suco, pizza (O ultimo elemento é ignorado)
print(lanche[2:]) #Até o final, pizza, pudim
print(lanche[:2]) #Vai até o 2 (desconsiderando o 2), hamburguer, suco
print(lanche[-2:]) #Vai começar na posiçao 2 detras para a frente (pizza), e acaba no fim (pudim)
print(len(lanche)) #4
print(sorted(lanche)) #Mostra  variavel em ordem, ele nao altera a tupla

#Tuplas sao IMUTAVEIS

#lanche[1] = 'Refrigerante' #Da erro
#print(lanche[1]) 

#Utilizando o for nas variaveis compostas
for comida in lanche: #Usando como itens
    print(f'Eu vou comer {comida}') #Eu vou comer {hamburguer}, {suco}, {pizza}, {pudim}
print('Comi pra caramba!')

#Outra maneira de utilizar o for
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}')
print('fim')

#Caso precise da posiçao tambem
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]}, na posiçao {cont}')
print('Termina')
#ou
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {pos}')
print('Fim')

#Junçao de Tuplas
a = (2,5,4)
b = (5,8, 1, 2)
c = a + b # O mais junta a Tupla
d = b + a
print(c) # 2,5,4,5,8,1,2
print(d) # 5,8,1,2,2,5,4
print(c.count(5)) #Vai mostrar quantas vezes aparece o numero 5 (2), se nao houver ele mostra 0
print(d.index(8)) #Mostra em que posiçao esta o objeto escolhido (8 esta na posiçao 1 (na tulpa D))
print(d.index(2)) #O 2 aparece duas vezes, mas pega a primeira ocorrencia (2 esta na posiçao 3 (na tupla D))
print(d.index(2,4)) # A partir da posiçao 4 mostrar qual posiçao aparece o 2 (2 aparece denovo na posiçao 4 (na tupla D))

#Apagando itens da tupla
pessoa = ('Silvia', 26, 'F', 60.00) #Podemos ter dados de tipos diferentes dentro da tupla
del(pessoa) #Apaga a tupla inteira, nao da para deletar apenas um item
print(pessoa)