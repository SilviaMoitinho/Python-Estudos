def cadastro():
    print('-'*30)
    print('{:^30}'.format('\033[34mNovo Cadastro\033[m'))
    print('-'*30)
    dados = dict()
    dados['nome'] = input('Nome: ').capitalize()
    dados['idade'] = input('Idade: ')
    return dados