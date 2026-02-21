"""
Crie a classe Churrasco, onde seja possivel informar quantas pessoas 
vao participar e mostre quanto de carne deve ser comprado, o custo total 
do churrasco e o preço por pessoa.
Condideramos:
Consumo padrao -- 400g por pessoa
Preço -- R$82.40 1kg
"""

from rich import print
from rich.panel import Panel

class Churrasco():
    def __init__(self, tit, quant):
        self.tit = tit
        self.quant = quant

    def analisar(self):
        quant_carne = 0.4 * self.quant
        total = quant_carne * 82.40
        preço_pessoa = total / self.quant
        return print(Panel(f" Analisando [green]{self.tit}[/] com [blue]{self.quant} convidados[/] \n Cada participante comera 0.4kg e cada kg custa R$82.40 \n Recomendo [blue]comprar{quant_carne:.2f}kg[/] de carne \n O custo total sera de [green]R${total:,.2f}[/] \n Cada pessoa pagara [yellow]R${preço_pessoa:.2f}[/] para participar", title=self.tit, expand=False))
    

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()