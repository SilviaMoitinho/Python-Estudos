def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero valido!\033[m')
        except KeyboardInterrupt:
            print('\033[33mO usuario preferiu nao informar os dados\033[m')
            n = 0
            break
    return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero valido!\033[m')
        except KeyboardInterrupt:
            print('\033[33mO usuario preferiu nao informar os dados\033[m')
            n = 0
            break
    return n