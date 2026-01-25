'''
faça um programa que leia o sexo de uma pessoa, mas so aceite
os valores 'M' e 'F'. Caso esteja errado, peça a digitaçao novamente ate ter um valor correto
'''

nome = str(input('Digite o seu nome: ')).strip()
sexo = str(input('Digite o seu sexo: [M/F]')).upper()

while sexo != 'F' and sexo != 'M':
    sexo = str(input('O que voce digitou nao é valido!\n'
    'Por favor escolha entre, [F] -> Feminino (Mulher) ou [M] -> Masculino (Homem)'
    '-> \n')).upper()


if sexo == 'F':
    print('Ficha criada: \n' \
    'nome = {} \n' \
    'sexo = FEMININO'.format(nome))
elif sexo == 'M':
    print('Ficha criada: \n' \
    'nome = {} \n' \
    'sexo = MASCULINO'.format(nome))
