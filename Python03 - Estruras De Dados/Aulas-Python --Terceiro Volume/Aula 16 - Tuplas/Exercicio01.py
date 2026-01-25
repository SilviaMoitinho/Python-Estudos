'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero a vinte. Seu programa devera ler um numero pelo teclado
(entre 0 e 20) e mostra-lo por extenso.
'''

extenso = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onde','Doze','Treze','Quatorze','Quinze','Dezasseis','Dezasete','Dezoito','Dezanove','Vinte')
n1 = 0
extenso1 = ''
n = int(input('Digite um numero entre 0 e 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Erro! Por favor digite um numero entre 0 e 20: '))
    else:
        break
print(f'{n} escrito fica: {extenso[n]}')