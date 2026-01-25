'''
Crie um programa que tenha uma tupla com varias palavras (nao usar acento).
Depois disso, voce deve mostrar para cada palavra, quais sao as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
cont = 0
for palavra in palavras:
    print(f'Na palavra {palavra.upper()} temos: ', end='')
    for c in range (0, len(palavra)):
        if palavra[c] in 'aeiou':
            print(f' {palavra[c]}', end='')
    print(end='\n')
