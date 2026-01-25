'''
Faça um programa que tenha uma funçao chamada escreva(),
que receba um texto qualquer como parametro e mostre 
uma mensagem com tamanho adaptavel
'''

def escreva(txt):
    c = len(frase)+2
    print('-'*c)
    print(f' {txt} ')
    print('-'*c)


frase = str(input('Digite uma frase: '))
escreva(frase)