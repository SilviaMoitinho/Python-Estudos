""""
Crie um programa que leia um numero de 0 a 9999 e mostre
na tela cada um dos digitos
digite um numero: 1834
unidade : 4
dezena : 3
centena : 8
milhar : 1
"""

"""
FORMA DE FAZER O EXERCICIO ESTAVA ERRADA, TEM DE USAR A FORMA MATEMATICA
numero = input('Digite um numero:')
unidade = numero [3]
print ('Unidade: {}'.format(unidade))
dezena = numero[2]
print ('Dezena: {}'.format(dezena))
centena = numero[1]
print ('Centena: {}'.format(centena))
milha = numero[0]
print ('Milha: {}'.format(milha))"""

#FORMA MATEMATICA
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o seu numero {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))