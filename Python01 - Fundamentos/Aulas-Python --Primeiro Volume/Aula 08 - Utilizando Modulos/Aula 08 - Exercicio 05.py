from math import sqrt
catop = float(input('Digite o cateto oposto:'))
catas = float(input('Digite o cateto adjacente:'))
hip = sqrt(catop*catop + catas*catas)
print ('A hipotenusa do seu triangulo é: {:.2f}'.format(hip))