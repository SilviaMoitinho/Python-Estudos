'''
Faça um programa que leia duas notas de um aluno e calcule sua media,
mostrando uma mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0: REPROVADO
- Media entre 5.0 e 6.9: RECUPERACAO
- Media acima de 7.0: APROVADO
'''
print('\033[35m-\033[m\033[34m=\033[m\033[35m-\033[m'*40)
print('                                Portal da ESCOLA')
print('\033[35m-\033[m\033[34m=\033[m\033[35m-\033[m'*40)
print('Veja qual é o seu STATUS de acordo com suas as notas: ')
n1 = float(input('Nota do Primeiro Trimestre:'))
n2 = float(input('Nota do Segundo Trimestre: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('STATUS:')
    print('\033[41mREPROVADO\033[m')
elif media >= 5.0 and media <= 6.9:
    print('STATUS:')
    print('\033[43mRECUPERAÇÃO\033[m')
else:
    print('STATUS:')
    print('\033[42mAPROVADO\033[m')