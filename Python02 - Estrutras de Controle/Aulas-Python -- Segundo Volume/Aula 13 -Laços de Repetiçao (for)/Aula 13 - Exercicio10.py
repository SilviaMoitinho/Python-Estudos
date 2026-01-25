'''
Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
'''
contagem = int(input('Quantas pessoas voce quer comparar? '))
mulheres_jovens = 0
mais_velha = 0
mais_velho = 0
soma_idades = 0
for c in range(1,contagem+1):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Quantos anos tem? '))
    sexo = str(input('Femino ou masculino?')).upper().strip()
    print('✿ ----------------- ✿ ------------------ ✿')
    soma_idades += idade
    if idade > mais_velho and sexo[0] == 'M':
        homem_velho = nome
        mais_velho = idade
    elif idade > mais_velha and sexo[0] == 'F':
        mulher_velha = nome
        mais_velha = idade
    if idade < 20 and sexo[0] == 'F':
        mulheres_jovens += 1

print('╰──────────────────❀')
media = soma_idades / contagem
print('A idade media do grupo é de {:.0f} anos'.format(media))
if mais_velho == 0:
    print('Nao existem homens na lista de cima, por isso te darei o nome e idade da mulher mais velha',end='')
    print('A mulher mais velha é a {} com {} anos'.format(mulher_velha, mais_velha))
else:
    print('O homem mais velho é o {} com {} anos'.format(homem_velho, mais_velho))
if mulheres_jovens == 0:
    print('Nesta lista nao existe mulheres com menos de 20 anos')
elif mulheres_jovens == 1:
    print('Existe apenas uma mulher com menos de 20 anos')
else:
    print('Existe {} mulheres com menos de 20 anos'.format(mulheres_jovens))