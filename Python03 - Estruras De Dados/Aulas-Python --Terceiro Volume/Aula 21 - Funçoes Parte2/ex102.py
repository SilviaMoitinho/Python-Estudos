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
    cont = n
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} ', end='')
            else:
                print(f'{c} x ', end='')
        print('= ', end='')
    for c in range(n, 0, -1):
        f *= c
    return f


print('-'*30)
print(fatorial(5))
help(fatorial)