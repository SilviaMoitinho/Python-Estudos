'''
Crie um programa que leia uma frase qualquer e diga se ela é 
um palindromo, desconsiderando os espaços
'''

frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# inverso = junto[::-1] (Alternativa) -- O inverso recebe o junto começando no inicio, até o fim, detras para a frente com -1
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao é um palindromo')