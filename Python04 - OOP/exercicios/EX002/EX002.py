"""
Crie a classe produto, onde podemos cadastrar nome e o
preço. Crie tambem um metodo que mostre uma etiqueta de preço de produto.
"""

from rich import print
from rich.panel import Panel

class Produto():
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        eti = Panel(f"{self.nome:^30}\n {"":-^30}\n {self.preço:.^30,.2f}", title="Produto",expand=False, style="black")
        return eti


p1 = Produto("Iphone 17 Pro Max", 1200)
print(p1.etiqueta())

p2 = Produto("Computador Gaming", 3800)
print(p2.etiqueta())