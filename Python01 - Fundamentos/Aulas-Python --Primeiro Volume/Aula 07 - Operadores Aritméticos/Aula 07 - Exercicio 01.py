#nome = input ('Qual é o seu nome? ')
#print ('Prazer em te conhecer {}.'.format(nome))
    #Podemos colocar entre {}, o formato do nosso objeto: {:20} - dara 20 espaços
    #{:<20} - dara 20 espaços para a esquerda, {:>20} - dara 20 espaços para a direita
    #{:^20} - coloca 20 espaços e deixara o objeto no centro
    #{:=^20} - coloca o objeto e o simbolo escolhido nos lados - =====Objeto=====

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
p = n1 ** n2
divint = n1 // n2
resdiv = n1 % n2                      #end= '' serve para nao quebrar a linha, ou seja este print e o proximo aparecerao na mesma linha quando executados
print ('A soma vale {}'.format(n1+n2),end='') #Pode fazer desse jeito o format, caso nao va utilizar a variavel soma
print ('A subtraçao entre os valores é: {}, da multiplicaçao é: {}, e da divisao é: {:.3f}'.format(sub, multi, div)) #{:.3f} significa 3 casas depois da virgula, ponto flutuante
print ('A potencia dos dois valores é: {}, a divisao inteiro é: {},\n e o resto da divisao é: {}'.format(p, divint, resdiv))
                                                                    # \n quebra a linha, ou seja a partir desse \n tudo sera exibido em outra linha quando executado