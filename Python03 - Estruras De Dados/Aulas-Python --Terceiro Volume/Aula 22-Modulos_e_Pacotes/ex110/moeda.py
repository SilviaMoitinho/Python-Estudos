def resumo(preço, t_aumento, t_diminui):
    print('-'*30)
    print('{:^30}'.format('Resumo Do Valor'))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{t_aumento}% de aumento: \t{aumentar(preço, taxa=t_aumento, form=True)}')
    print(f'{t_diminui}% de reduçao: \t{diminuir(preço, taxa=t_diminui, form=True)}')
    print('-'*30)


def moeda(preço=0, moeda='R$'):
    res = f'{moeda}{preço:.2f}'.replace('.',',')
    return res


def aumentar(preço=0, taxa=0, form=False):
    res = preço + (preço * taxa /100)
    if form:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, taxa=0, form=False):
    res = preço - (preço * taxa / 100)
    if form:
        return moeda(res)
    else:
        return res


def dobro(preço=0, form=False):
    res = preço * 2
    if form:
        return moeda(res)
    else:
        return res


def metade(preço=0, form=False):
    res = preço / 2
    if form:
        return moeda(res)
    else:
        return res
