def menu():
    print('-'*30)
    print('{:^30}'.format(' Menu Principal'))
    print('-'*30)
    print('[ 1 ] \033[32mVer pessoas cadastradas\033[m')
    print('[ 2 ] \033[34mCadastrar nova pessoa\033[m')
    print('[ 3 ] \033[31mSair do Sistema\033[m')
    while True:
        try:
            n = int(input('-> '))
            if n > 3:
                print('\033[33mPor favor. Escolha uma das opçoes acima.\033[m')
            else:
                break
        except (ValueError, TypeError):
            print('\033[31mDigite um valor valido!\033[m')
    return n