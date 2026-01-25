'''
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionario se 
por acaso o CTPS for diferente de zero, o dicionario recebera
tambem o ano de contrataçao e o salario. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] =datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de Contrataçao: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')