"""
Crie uma classe ControleRemoto, onde vamos simular
o funcionamento de um controle simples (canal, volume
e liga/desliga)
"""

from rich import print
from rich.panel import Panel

class ControleRemoto():
    def __init__(self):
        self.tv_ligada = False
        self.canal = 1
        self.volume = 1
    
    def mostrar_canais(self):
        tot_canais = 5
        self.canais = ""
        for i in range(1, tot_canais+1):
            if i == self.canal:
                self.canais += f"[yellow]{i}[/] "
            else:
                self.canais += f"{i} "
        return f"Canal {self.canais}"

    def vol(self):
        tot_volume = 10
        volu = ""
        for v in range(1, tot_volume+1):
            if v == self.volume:
                volu += f"[red]{v}[/] "
            else:
                volu += f"{v} "
        return f"Volume {volu}"

    def tv(self):
        if self.tv_ligada == True:
            print("\n"*80)
            print(Panel(f"Canal {self.mostrar_canais()} \n Volume {self.vol()}", title="[TV]", style="green", width=40))
        else:
            print("\n"*80)
            print(Panel(" A TV esta deligada",title="[Tv]", style="red", width=40))

    def menu(self, limpar="\n"*80):
        self.tv()
        while True:
            r = input("< CH >  - Vol +  ")
            if r == "0":
                break
            if r == "@" and self.tv_ligada == True:
                self.tv_ligada = False
                self.tv()
            elif r == "@" and self.tv_ligada == False:
                self.tv_ligada = True
                self.tv()
            if r == ">":
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1
                self.tv()
            elif r == "<":
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1
                self.tv()
            if r == "+":
                if self.volume == 10:
                    self.volume = 1
                else:
                    self.volume += 1
                self.tv()
            elif r == "-":
                if self.volume == 1:
                    self.volume = 10
                else:
                    self.volume -= 1
                self.tv()
        


c1 = ControleRemoto()
c1.menu()