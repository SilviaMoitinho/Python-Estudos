diaria = int(input('Quantos dias alugados:'))
km = float(input('Quantos Km rodados:'))
dp = diaria * 60
kmp = km * 0.15
total = dp + kmp
print ('Total a pagar é de R${:.2f}'.format(total))