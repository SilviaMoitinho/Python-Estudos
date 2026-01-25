'''
Crie um programa que leia uma frase qualquer e diga se ela é 
um palindromo, desconsiderando os espaços
'''
contagem = 0
contador = 0
frase = str(input('Escreva uma frase: ')).upper().replace(' ', '')
caracteres = len(frase)-1
inteiro = int(len(frase)/2)

for c in range(0, inteiro):
    if frase[contador] == frase[caracteres]:
        contador = contador + 1
        contagem = contagem + 1
        caracteres = caracteres - 1
    else:
        break

if contagem == inteiro:
    print('Essa frase é um palindromo')
else:
    print('Essa frase NAO é um palindromo')