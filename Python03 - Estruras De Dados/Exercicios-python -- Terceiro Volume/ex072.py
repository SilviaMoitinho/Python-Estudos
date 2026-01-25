'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero a vinte. Seu programa devera ler um numero pelo teclado
(entre 0 e 20) e mostra-lo por extenso.
'''

cont = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis',
        'Sete','Oito','Nove','Dez','Onde','Doze','Treze',
        'Quatorze','Quinze','Dezaseis','Dezasete','Dezoito',
        'Dezanove','Vinte')
while True:
    num = int(input('Digite um  numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente', end='')
print(f'Voce digitou o numero {cont[num]}')