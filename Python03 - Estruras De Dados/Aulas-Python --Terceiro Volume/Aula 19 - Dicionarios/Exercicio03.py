'''
Crie um programa que leia nome, ano de nascimento e carteira
de trabalho e cadastre-os (com idade) em um dicionario se 
por acaso o CTPS for diferente de zero, o dicionario recebera
tambem o ano de contrataçao e o salario. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
trabalhador['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contrato'] = int(input('Ano de contrataçao: '))
    trabalhador['salario'] = float(input('Salario: R$'))
    trabalhador['aposentadoria'] = (35 - (date.today().year - trabalhador['contrato'])) + trabalhador['idade']
print('-'*30)
for k,v in trabalhador.items():
    print(f'{k} tem valor {v}.')