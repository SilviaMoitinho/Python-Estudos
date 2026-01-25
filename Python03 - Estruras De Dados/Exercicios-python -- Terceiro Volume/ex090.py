'''
Faça um programa que leia nome e média de um aluno,
guardando tambem a situaçao em um dicionario.
No final, mostre o conteudo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['média']:
    aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f'  - {k} é igual a {v}')