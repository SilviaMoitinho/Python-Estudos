'''
Crie um programa que tenha uma tupla unica com nomes e produtos
e seus respetivos preços, na sequencia. No final, mostre uma
listagem de preços, organizando os dados de forma tabular.
'''
itens = ('Lapis', 1.75, 
         'Borracha', 2.00, 
         'Caderno', 15.90, 
         'Estojo', 25.00, 
         'Transferidor', 4.20, 
         'Compasso', 9.99, 
         'Mochila', 120.32, 
         'Canetas', 22.30, 
         'Livro', 39.90)
print('-'*52)
print('{:^52}'.format('Listagem de Preços'))
print('-'*52)
for c in range (0, len(itens)):
    if c % 2 == 0:
        print('{:.<12}'.format(itens[c]), end='')
        print('{:.>33}'.format('R$'), end='')
        print('{:7}'.format(itens[c+1]))
print('-'*52)