"""
Crie a classe Caneta, que simule o funcionamento de uma
caneta colorida, podendo escrever frases na cor relativa
"""

from rich import print

class Caneta():
    def __init__(self, cor):
        self.cor = str(cor).upper()
        self.tampada = True

    def destampar(self):
        self.tampada = True

    def tapar(self):
        self.tampada = False
    
    def quebrar(self, quant):
        print("\n"*quant)

    def escrever(self, txt):
        if self.tampada == True:
            if self.cor == "AZUL":
                print(f"[blue]{txt}[/] ", end='')
            if self.cor == "VERDE":
                print(f"[green]{txt}[/] ", end='')
            if self.cor == "VERMELHO":
                print(f"[red]{txt}[/] ", end='')
        else:
            if self.cor == "AZUL":
                print("A [blue]caneta azul[/] esta tapada")
            if self.cor == "VERDE":
                print("A [green]caneta verde[/] esta tapada")
            if self.cor == "VERMELHO":
                print("A [red]caneta vermelha[/] esta tapada")


c1 = Caneta("Azul")
c2 = Caneta("verde")
c3 = Caneta("Vermelho")
c1.destampar()
c2.destampar()
c3.destampar()
c2.quebrar(1)
c1.escrever("Ola mundo,")
c2.escrever("o curso de Python")
c3.escrever("é muito legal!")
c1.quebrar(2)
c1.tapar()
c1.escrever("Fim!")
