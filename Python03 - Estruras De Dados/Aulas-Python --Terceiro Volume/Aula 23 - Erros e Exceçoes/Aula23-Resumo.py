# Tratamentos de erros

try: #Pedir ao programa para tentar fazer
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:#Caso de erro, ele mostra a mansagem - Exception as erro mostra o erro
    print(f'Problema encontrado foi {erro.__class__}')# .__class__ nos diz a classe do erro
else: #Caso de certo, mostra a mensagem (é opcional)
    print(f'O resultado é {r:.1f}')
finally: #Caso de certo ou errado (é opcional)
    print('Volte sempre! Muito obrigado.')

# Um mesmo try pode ter varios except

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Se o erro foi Erro de valor, ou Erro de tipo
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError: #Se o erro for tentar dividir o 0
    print('Nao é possivel dividir um numero por zero')
except KeyboardInterrupt: # Se o usuario parar o programa (ctr+c)
    print('O usuario preferio nao informar os dados.')    
else: 
    print(f'O resultado é {r:.1f}')
finally: 
    print('Volte sempre! Muito obrigado.')