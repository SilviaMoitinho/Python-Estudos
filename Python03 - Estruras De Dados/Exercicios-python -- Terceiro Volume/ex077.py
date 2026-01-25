'''
Crie um programa que tenha uma tupla com varias palavras (nao usar acento).
Depois disso, voce deve mostrar para cada palavra, quais sao as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #Se precisar, podemos adicionar as vogais com acento
            print(letra, end=' ')
