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
    di = {}
    di['total'] = len(n)
    di['maior'] = max(n)
    di['menor'] = min(n)
    di['media'] = sum(n) / len(n)
    if sit == True:
        if di['media'] >= 7:
            di['situaçao'] = 'BOA'
        elif di['media'] < 7 and di['media'] >= 5:
            di['situaçao'] = 'Razoavel'
        else:
            di['situaçao'] = 'Ruim'
    return di


resp = notas(5.5,2.5,1.5, sit=True)
print(resp)
