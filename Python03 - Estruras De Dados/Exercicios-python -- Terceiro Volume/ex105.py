'''
Faça um programa que tenha uma funçao notas() que pode receber varias
notas de alunos e vai retornar um dicionario com a seguintes informaçoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situaçao(opcional)
Adicione tambem as docstrings da funçao.
'''

def notas(*n, sit=False):
    """
    -> Funçao para analisar notas e situaçoes de varios alunos
    :param n: Uma ou mais notas de alunos (aceita varias)
    :param sit: Valor opcional, indicando se deve ou nao adicionar a situaçao
    :return: dicionario com varias funçoes sobre a situaçao da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situaçao'] = 'Boa'
        elif r['media'] >= 5:
            r['situaçao'] = 'Razoavel'
        else:
            r['situaçao'] = 'Ruim'
    return r


#Programa Principal
resp = notas(5.5,2.5,9,8.5, sit=True)
print(resp)