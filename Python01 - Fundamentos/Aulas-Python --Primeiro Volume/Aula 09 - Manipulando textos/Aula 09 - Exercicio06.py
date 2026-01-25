"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente
exemplo: Ana Maria de Souza
primeiro : Ana
ultimo: Souza
"""
nomecompleto = str(input('Digite o seu nome completo: ')).strip()

primeiro = nomecompleto.split()
print('Primeiro nome:{}'.format(primeiro[0]))
print('Ultimo nome:{}'.format(primeiro[-1]))