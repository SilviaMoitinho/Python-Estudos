from funçoes import menu, cadastro, listagem

while True:
    n = menu.menu()
    while True:
        if n == 1:
            listagem.mostrarlista()
            break
        elif n == 2:
            pessoa = cadastro.cadastro()
            listagem.receber(pessoa)
            break
    if n == 3:
        print('\033[36mObrigado por utilizar nosso sistema.')
        print('     \033[35mVolte Sempre!\033[m')
        break