'''
Faça um programa que leia o ano de nascimento de um joveme informe,
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se ja passou o tempo do alistamento
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
'''
from time import sleep
from datetime import date

print('-+-'*40)
print('Alistamento ao Serviço Militar')
print('-+-'*40)

print('Verifique o seu estado de alistamento:')
n = str(input('Nome: '))
print('Data de nascimento: ')
dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))
gen = str(input('Genero(F/M): ')).upper()
data_pessoal = date(ano, mes, dia)
hoje = date.today()
idade = hoje.year - data_pessoal.year
if (hoje.month, hoje.day) < (data_pessoal.month, data_pessoal.day):
    idade -= 1 # -= Significa idade = -1

if gen == 'MASCULINO':
    print('Criando a sua ficha...')
    sleep(2)

    print('-'*40)
    print('Ficha Pessoal:')
    print('Nome = {}'.format(n))
    print('Data de nascimento = {}'.format(data_pessoal))
    print('Idade = {}'.format(idade))
    print('-'*40)

    if idade < 18:
        print('\033[43mSTATUS: PENDENTE\033[m')
        print('Ainda \033[1;31mNAO esta na hora\033[m de se alistar ao serviço militar')
        print('Faltam \033[1;33m{} anos\033[m para se alistar.'.format(18-idade))
        print('Voce tera que se alistar em {}'.format(hoje.year + (18 - idade)))
    elif idade == 18:
        print('\033[42mSTATUS: ACEITE\033[m')
        print('Ja pode se alistar!')
    elif idade > 18:
        print('\033[41mSTATUS: ATRASADO\033[m')
        print('ja passou o tempo do seu alistamento!')
        print('Voce esta com atraso de \033[1;31m{} anos\033[m.'.format(idade - 18))
        print('Voce deveria ter se alistado em {}'.format(hoje.year - (idade - 18)))

if gen == 'FEMININO':
    print('O alistamento nao é obrigatorio para mulheres!')
    if idade >= 18:
        print('Idade: {} anos'.format(idade))
        print('Se voce quiser ja pode se alistar!')
    elif idade < 18:
        print('Idade: {} anos')
        print('Voce ainda nao pode se alistar, podera realizar o alistamento se desejar em {}'.format(hoje.year + (18 - idade)))