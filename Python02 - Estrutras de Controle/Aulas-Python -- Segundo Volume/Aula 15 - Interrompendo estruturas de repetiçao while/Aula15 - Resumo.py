# looping infinito
'''cont = 1
while True:
    print(cont,'->', end='')
    cont += 1
print('Acabou')'''

# While utilizando flags
n = 0
while n != 999:
    n = int(input('Digite um numero: '))

# Tetar e interromper
n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s)) Forma antiga
print(f'A soma vale {s}') # Nova forma de formatar, f strings

# F strings
nome = 'Silvia'
idade = 26
salario = 9937.35
print(f'O {nome:20} tem {idade} anos e ganha R${salario:.2f}') # Python 3.6 +
            #Aparecer com 20 espaços            formatar para 2 casas decimais
