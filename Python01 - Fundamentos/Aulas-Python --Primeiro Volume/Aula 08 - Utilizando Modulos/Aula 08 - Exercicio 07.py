import random
n1 = input ('Primeiro nome para sorteio:')
n2 = input ('Segundo nome para sorteio:')
n3 = input ('Terceiro nome para sorteio:')
sorteio = random.choice([n1, n2, n3])
print ('O ganhador foi: {}. Parabens!'.format(sorteio))