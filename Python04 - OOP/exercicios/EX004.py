"""
Crie a classe Livro, que vai simular a passagem
de um livro. Considerando tambem se o usuario
chegou ao fim da leitura.
"""

from rich import print
from time import sleep

class Livro():
    def __init__(self, nome, pag):
        self.nome = nome
        self.pag = pag
        print(f":book: [blue]Voce acabou de abrir o livro[red] {self.nome}[/] que tem [green]{self.pag} paginas[/] no total. \n Voce agora esta na [/][yellow]pagina 1[/]")

    def avancar_pagina(self, quant, lista=[2]):
        cont = 0
        pag = lista[0]
        for c in range(cont, quant):
            if pag > self.pag:
                break
            print(f" Pag{pag} ➜ ", end='')
            pag += 1
            cont += 1
            sleep(1)
        lista[0] = pag
        print(f"[blue] Voce avançou {cont} paginas e agora esta na [/][yellow]pagina {pag-1}[/]")
        if pag-1 >= self.pag:
            print(f"[red]Voce chegou ao final do livro {self.nome}[red]")



l1 = Livro('10 coisas que aprendi na vida', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(100)