'''
A confederaçao Nacional de Nataçao precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER
'''

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificaçao: MIRIM')
elif idade <= 14:
    print('Classificaçao: INFANTIL')
elif idade <= 19:
    print('Classificaçao: JUNIOR')
elif idade <= 20:
    print('Classificaçao: SENIOR')
else:
    print('Classificaçao: MASTER')