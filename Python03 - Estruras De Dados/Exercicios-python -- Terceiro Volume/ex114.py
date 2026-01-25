'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site pudim nao esta acessivel no momento!')
else:
    print('Deu certo!')
    print(site.read()) # Consguimos ler o conteudo html do site