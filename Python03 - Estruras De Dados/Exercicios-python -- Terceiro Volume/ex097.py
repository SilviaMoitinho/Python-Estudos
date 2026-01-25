'''
Faça um programa que tenha uma funçao chamada escreva(),
que receba um texto qualquer como parametro e mostre 
uma mensagem com tamanho adaptavel
'''

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')