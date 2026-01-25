'''
Refaça o desafio 035 dos triangulos, 
acrescentando o recurso de mostrar que tipo de triangulo sera formado:
- Equilaterio: Todos os lados iguais
- Isosceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
'''

print('Insira 3 segmentos e veja qual triangulo forma:')
r1 = float(input('Primeiro Segmento -> '))
r2 = float(input('Segundo Segmento -> '))
r3 = float(input('Terceiro Segmento -> '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('Forma um triangulo \033[31mEQUILATERO\033[m')
    elif r1 == r2 or r2 == r3:
        print('Forma um triangulo \033[32mISOSCELES\033[m')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Forma um triangulo \033[33mESCALENO\033[m')
else: 
    print('Os Sagmentos NAO podem formar um triangulo!')