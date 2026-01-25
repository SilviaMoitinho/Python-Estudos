import random
n1 = input ('Primeiro aluno:')
n2 = input ('Segundo aluno:')
n3 = input ('Terceiro aluno:')
n4 = input ('Quarto aluno:')
lista = [n1, n2, n3, n4] #No python para criar listas elas tem estar entre []
random.shuffle(lista) #embaralha o que colacamos entre ()
print ('A odem de execuçao sera:') #se eu colocar o format, ele nao mostra a lista
print (lista)