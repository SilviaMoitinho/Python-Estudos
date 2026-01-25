#Criando funçoes com parametros
def soma(a,b):
    print(f'a= {a}, b= {b}')#Podemos usar prints formatados com os parametros que criamos
    s = a+b
    print(f'A soma A + B = {s}')
#Tem que dar duas linhas de espaço entre o def e o programa principal
#Programa Principal
soma(3,2) #Esses numeros sao parametros
soma(2,9)
#soma(4) #Vai dar erro, porque estamos so colocando 1 parametro, e na def esta 2
soma(b=4,a=5) #podemos mudar a ordem que a def recebe os parametros, contando que fique explicito (a=x)

#Desempacotar parametros (TUPLAS)
def contador(*num): #Este * diz que nao sabemos quantos parametros a nossa def vai receber
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    tam = len(num) # Podemos criar uma variavel para guardar o tamanho do parametro(quantos ele recebeu)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')
                    #Ele vai criar tuplas, com os paremtros dentro

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

#Usando def com Listas
def dobra(lst): #Tudo que eu fizer na minha lista em def, vai interferir na minha lista no codigo principal (valores)
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores) # Vai aparecer os valores dobrados