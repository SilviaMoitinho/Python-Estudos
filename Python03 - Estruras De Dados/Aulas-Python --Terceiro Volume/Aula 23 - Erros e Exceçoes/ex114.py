'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import requests

try:
    resp = requests.get('http://pudim.com.br', timeout=5)
    if resp.status_code == 200:
        print('O site rodou perfeitamente')
except:
    print('\033[31mNao consegui acessar o site\033[m')