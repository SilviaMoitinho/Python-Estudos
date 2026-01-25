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
