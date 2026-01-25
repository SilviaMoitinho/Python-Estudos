m = float(input('Escreva em metros o numero que voce quer: '))
dm = m * 10
c = int(m * 100)
mm = int(m * 1000)
dam = m / 10
hm = m / 100
km = m / 1000
print ('valor em kilometro: {}km'.format(km))
print ('valor em hectometro: {}hm'.format(hm))
print ('valor em decametro: {}dam'.format(dam))
print ('valor em metros: {}m'.format(m))
print ('Valor em decimetros: {:.0f}dm'.format(dm))
print ('valor em centimetros: {}cm'.format(c))
print ('valor em milimetros: {}mm'.format(mm))