'''
faça um programa que leia o sexo de uma pessoa, mas so aceite
os valores 'M' e 'F'. Caso esteja errado, peça a digitaçao novamente ate ter um valor correto
'''

sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF': # Enquanto o sexo nao tem 'M ou F'
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
