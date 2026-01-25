print ('Python Pintura')
print ('Calcule quantos listros de tinta voce vai precisar para pintar a sua parede!')
print ('============================================================================')
c = float(input('Qual a altura da sua parede? '))
l = float(input('Qual a largura da sua parede? '))
a = int(l * c)
t = a / 2
print ('Para a sua parede de {}m quadrados, vai precisar de {:.0f}L de tinta'.format(a, t))