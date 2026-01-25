import moeda

p = float(input('Digite o preço: R$'))

print(f'O preço {moeda.moeda(p)} com um aumento de 10% fica {moeda.aumentar(p,10)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')