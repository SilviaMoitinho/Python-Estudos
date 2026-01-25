'''
Faça um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media acima de 7.0: APROVADO
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {} e {}, a nota do aluno é {}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno esta em RECUPERACAO')
elif media < 5:
    print('Aluno esta REPROVADO')
else:
    print('Aluno esta APROVADO')