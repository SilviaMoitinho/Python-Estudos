'''
Modifique as funçoes que foram criadas no desafio 107 para que elas aceitem um parametro
a mais, informando se o valor retornado por elas vai ser ou nao formatado pela funçao
moeda(), desenvolvida no desafio 108
'''

import moeda

p = float(input('Digite o preço: R$'))

print(f'O preço {moeda.moeda(p)} com um aumento de 10% fica {moeda.aumentar(p,10,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')