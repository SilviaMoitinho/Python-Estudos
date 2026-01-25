"""

Faça um programa que leia uma frase
pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posiçao ela aparece a primeira vez
- Em que posiçao ela aparece a ultima vez
"""

frase = str(input('Diga alguma coisa: ')).strip()

frasem = frase.upper().count('A')
print('Na sua frase existe {} letras A'.format(frasem))

frase_a = frase.upper().find('A')
print('Ela aparece na primeira vez na posiçao: {}'.format(frase_a))

frase_r = frase.upper().rfind('A')
print('Ela aparece a ultima vez na posiçao: {}'.format(frase_r))