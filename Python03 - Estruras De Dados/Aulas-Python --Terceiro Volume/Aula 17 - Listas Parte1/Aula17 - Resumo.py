#Listas sao mutaveis, podemos alterar quamquer valor
num = [2,5,9,1]
num[-1] #Vai para o ultimo elemento da lista
num[2] = 3 #Mudou o 9 para 3
'''num[4] = 7 #Da erro, nao podemos adicionar valores dessa maneira'''
num.append(7) #Maneira correta de adicionar elementos na lista
num.sort() #Coloca em ordem
num.sort(reverse=True) #Coloca ao contrario
num.insert(2, 0) #Insere valores na posiçao indicada, aqui a posiçao é 2, 
                    #e o numero escolhido é 0, entao entre a posiçao 1 e 2 vai adicionar uma 
                    # posiçao 2 e andar para a frente uma casa
num.pop() #Elimina o ultimo elemento
num.pop(2) #Elimina o elemento 2
num.remove(2) #Elimina o primeiro numero 2, se tiver mais eles se mantem
print(num)
print(f'Essa lista tem {len(num)} elementos') #Diz quantos elementos tem a lista

#Procurando na lista
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 4')

#Criando uma lista vazia
valores = [] #ou valores = list()

#Mostrando a lista 'bonitinha'
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

print('')

#Mostrando a lista com posiçoes
for c, v in enumerate(valores):
    print(f'Na posiçao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.') 

#Ler valores pelo teclado e colocar na lista
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

#Quando igualamos uma lista com a outra, o que muda em uma, tambem muda na outra
a = [2,3,4,7]
b = a #Igualamos as listas
b[2] = 8 #mudamos a lista b, mas elas doram igualadas, a lista A tambem vai receber 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Para criar uma copia, copiar os valores de uma lista para a outra e nao igualar elas
b = a[:] #A lista b recebe todos os valores da lista A