import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade do {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% fica {moeda.aumentar(p,10)}')