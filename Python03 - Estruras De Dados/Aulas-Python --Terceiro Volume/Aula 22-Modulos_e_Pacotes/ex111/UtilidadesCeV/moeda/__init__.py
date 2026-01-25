def resumo(preço, t_aumento, t_diminui):
    print('-'*30)
    print('{:^30}'.format('Resumo Do Valor'))
    print('-'*30)
    print('Preço Analisado:', end='')
    print('{:>15}'.format(moeda(preço)))
    print('Dobro do preço:', end='')
    print('{:>15}'.format(dobro(preço, True)))
    print('Metade do preço:', end='')
    print('{:>15}'.format(metade(preço, True)))
    print(f'{t_aumento}% de aumento:', end='')
    print('{:>15}'.format(aumentar(preço, taxa=t_aumento, form=True)))
    print(f'{t_diminui}% de reduçao:', end='')
    print('{:>15}'.format(diminuir(preço, taxa=t_diminui, form=True)))
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
