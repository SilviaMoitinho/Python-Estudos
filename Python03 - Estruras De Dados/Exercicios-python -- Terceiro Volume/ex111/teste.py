'''
Crie um pacote chamado UtilidadesCeV que tenha dois modulos internos
chamados moeda e dado. Transfira todas as funcionalidades nos desafios anteriores
para o primeiro pacote e mantenha tudo funcionando.
'''

from UtilidadesCeV import moeda

p = float(input('Digite o preço: R$'))

moeda.resumo(p)