'''
Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar
No final, mostre:
a) Quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos
'''

mais18 = homens = mulheres20 = 0

print('━━━━━━━━━━ × ━━━━━━━━━━')
print('    Analise De Dados')
print('━━━━━━━━━━━━━━━━━━━━━━━')

while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if sexo == 'F' or sexo == 'M':
            break
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    while True:
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if r == 'S' or r == 'N':
            break
    if r == 'N':
        break
print('*'*20)
print('')
print('*'*20)
print('Final do programa')
print(f'Total de \033[31mpessoas\033[m com \033[31m+18\033[m anos: \033[1;31m{mais18}\033[m')
print(f'Total de \033[33mhomens\033[m cadastrados: \033[1;33m{homens}\033[m')
print(f'Total de \033[32mmulheres\033[m com \033[32mmenos de 20\033[m anos: \033[1;32m{mulheres20}\033[m')