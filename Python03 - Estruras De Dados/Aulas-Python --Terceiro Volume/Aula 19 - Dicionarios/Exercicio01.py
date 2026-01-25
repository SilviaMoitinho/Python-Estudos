'''
Faça um programa que leia nome e média de um aluno,
guardando tambem a situaçao em um dicionario.
No final, mostre o conteudo da estrutura na tela.
'''

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Média'] > 7.0:
    aluno['Status'] = 'Aprovado'
else:
    aluno['Status'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}.')