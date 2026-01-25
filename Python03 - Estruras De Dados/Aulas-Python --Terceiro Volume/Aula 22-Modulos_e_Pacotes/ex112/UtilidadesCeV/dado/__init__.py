def leiadinheiro(msg):
    p = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
                p = n
                break
        else:
            print('\033[31mErro! Digite um valor valido!\033[m')
    return float(p.replace('.',','))