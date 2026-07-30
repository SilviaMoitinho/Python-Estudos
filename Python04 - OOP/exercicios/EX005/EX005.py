"""
Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos
favoritos de uma pessoa. Crie tambem um método que permita mostrar a ficha desse gamer.
"""

from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogo, fav=[]):
        jogo = str(jogo).capitalize()
        fav.append(jogo)
        self.favoritos = fav

    def ficha(self):
        p = '\n🎮 '.join(map(str, self.favoritos))
        print(Panel(f"Nome real: [green]{self.nome} [/]\nJogos favoritos: \n🎮 [blue]{p}[/]", title=f"Jogador <{self.nick}>", style="black", width=30, ))

j1 = Gamer("Silvia", "Uma_Noob")
j1.add_favoritos("The Sims")
j1.add_favoritos("Minecraft")
j1.add_favoritos("gta")
j1.ficha()

j2 = Gamer("Jean", "Mestre_dos_jogos")
j2.add_favoritos("call of duty")
j2.add_favoritos("Fortnite")
j2.add_favoritos("Last of us")
j2.add_favoritos("need for speed")
j2.ficha()