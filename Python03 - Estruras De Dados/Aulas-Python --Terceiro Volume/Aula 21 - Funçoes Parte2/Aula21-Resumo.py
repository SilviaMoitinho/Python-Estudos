# Interactive Help 
help(input) #Vai mostrar um documento da funçao desesejada, podemos usar para bibliotecas tambem
print(input.__doc__) #Tambem vai mostrar um documento da funçao escolhida

#Docstring - serve para criar a documentaçao das funçoes que criamos
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno
    Funçao criada por Silvia
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador) # Vai mostrar a documentaçao que escrevemos

#Parametros Opcionais
def somar (a=0, b=0,c=0): #Se os parametros nao receberem nenhum valor, eles valem 0
    """ 
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Funçao criada por Silvia
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5) #Assim todos esses exemplos vai rodar sem problemas
somar(8,4)
somar (c=3, a=2)
somar()

#Escopo de variaveis

def teste():
    x = 8 #Variavel x tem escopo global, ela so funciona dentro da def teste
    print(f'Na funçao teste, n vale {n}.')
    print(f'Na funçao teste, x vale {x}')


'''Programa Principal'''
n = 2 #Variavel n tem escopo global, ela dentro e fora de def
print(f'No programa principal, n vale {n}')
teste()
'''print(f'No programa principal, x vale{x}')''' #Se tentarmos chamar uma variavel local fora da sua def, da erro

#Utilizando a variavel global com a funçao (global)
def funçao():
    global a #Utilizando essa funçao, o programa nao vai criar uma variavel local a, e sim utilizar a global
    a = 7
    n1 = 4 # Esse n1 é diferente de o n1 golval em baixo
    print(f'N1 dentro vale {n1}')
    print(f'A dentro vale {a}')


n1 = 2 # Esse é global
a = 4
funçao()
print(f'N1 fora vale {n1}')
print(f'A fora vale {a}') #No final a vai valer 7, porque alterou dentro da def

#Return (Retorno de valores)

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s #Vai retorar um valor


r1 = somar(3, 2, 5) # Coloca o valor dentro dessas variaveis
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')

# Exemplo pratico RETURN numero

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2}, {f3}')

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

#Exemplo pratico RETURN booleano

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
print(par(num)) # Vai dar verdadiro ou falso
if par(num): # Se for verdadeiro
    print('é par')
else:
    print('nao é par')