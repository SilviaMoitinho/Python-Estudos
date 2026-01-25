print ('Bem vindo ao TransferPython!')
print ('============================')
print ('Cotaçao do Dolar HOJE: 5.30$')
r = float(input('Reais que pretende converter: '))
d = r / 5.30
eu = r / 6.14
print ('Os seus R${}, podem ser convertidos em US${:.2f}'.format(r, d))
print ('Ou os seus R${}, podem ser convertidos em €{:.2f}'.format(r, eu))
print ('Obrigado por escolher o TransferPython!')