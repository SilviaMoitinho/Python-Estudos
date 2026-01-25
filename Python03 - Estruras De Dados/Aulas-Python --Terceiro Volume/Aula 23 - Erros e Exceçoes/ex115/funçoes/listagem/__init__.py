listagem = [{'nome': 'Ana', 'idade': '20'}, {'nome': 'Joao', 'idade': '18'}]

def receber(dici: dict):
    listagem.append(dici)


def mostrarlista():
    print('-'*30)
    print('{:^30}'.format('\033[32mPessoas Cadastradas\033[m'))
    print('-'*30)
    print(f'Nome:    \tIdade:')
    for c in range(0, len(listagem)):
        print(f'{listagem[c]['nome']}   \t{listagem[c]['idade']}')