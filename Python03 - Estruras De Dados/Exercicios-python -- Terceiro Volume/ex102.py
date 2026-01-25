'''
Crie um programa que tenha uma funçao fatorial() que receba
2 parametros: o primeiro que indique o numero a calcular
e o outro chamado show, que sera um valor logico(opcional)
indicando se sera mostrado ou nao na tela o processo de
calculo do fatorial
'''

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado
    :param show: (Opcional) Mostrar ou nao a conta
    :return: O valor do fatorial de um numero n
    Criado por Silvia
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
print(fatorial(5, show=True))
help(fatorial)