from math import sqrt, ceil #Apenas estes dois modulos foram importados da biblioteca math
#import math #Assim ele importa a biblioteca inteira
num = int(input('Digite um numero:'))
raiz = sqrt(num) #Se importar um modulo especifico nao precisa mais colocar math.
#raiz = math.sqrt(num) #Se importar a biblioteca inteira, tem de colocar o math.
print ('A raiz quadrada de {} é {}'.format(num, ceil(raiz)))