'''
A confederaçao Nacional de Nataçao precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima de 25 anos: MASTER
'''
from time import sleep
from datetime import date, datetime

print('\033[34m-\033[m\033[36m_\033[m\033[34m-\033[m'*30)
print('Confederaçao Nacional de Nataçao')
print('\033[34m-\033[m\033[36m_\033[m\033[34m-\033[m'*30)
print('Digite a sua data de nascimento para saber a sua categoria')
dia = int(input('Dia -> '))
mes = int(input('Mes -> '))
ano = int(input('Ano -> '))
data_nascimento = date(ano, mes, dia)
hoje = date.today()
idade = hoje.year - data_nascimento.year
if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

print('\033[4mCalculando a sua categoria, aguarde...\033[m')
sleep(2)

if idade <= 9:
    print('Categoria: \033[42mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('Categoria: \033[43mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Categoria: \033[44mJUNIOR\033[m')
elif idade >= 20 and idade <=25:
    print('Categoria: \033[45mSENIOR\033[m')
else:
    print('Categoria: \033[41mMASTER\033[m')
