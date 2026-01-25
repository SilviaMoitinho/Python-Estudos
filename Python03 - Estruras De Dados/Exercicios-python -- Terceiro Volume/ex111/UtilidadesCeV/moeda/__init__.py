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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('Resumo Do Valor'.center(30))
    print('-'*30)
    print(f'Analisando o preço: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de reduçao: \t{diminuir(preço, taxar, True)}')
    print('-'*30)