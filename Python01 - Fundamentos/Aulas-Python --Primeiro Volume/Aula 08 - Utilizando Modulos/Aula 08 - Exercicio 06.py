import math
ang = float(input('Qual é o angulo:'))
cosseno = math.cos(math.radians(ang)) #Podemos usar funçoes aninhadas com outras
tangente = math.tan(math.radians(ang)) #Radians serve para converter o valor de graus para radianos
seno = math.sin(math.radians(ang))
print('Com o angulo de {}, pude calcular o cosseno: {:.2f} \n o seno: {:.2f} \n e a tangente: {:.2f}'.format(ang, cosseno, seno, tangente))