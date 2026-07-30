"""
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie tambem um metodo que permita ao funcionario se apresentar.
"""

from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Video"

    def __init__(self, nome, setor, cargo):
        # Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentaçao(self) -> str: # significa que essa funçao retorna uma string
        return f":handshake: Ola, sou [blue]{self.nome}[/blue] e sou {self.setor} do setor {self.cargo} da empresa {Funcionario.empresa}" # Ou {self.__class__.empresa}


c1 = Funcionario("Maria", "Administraçao", "Diretora")
print(c1.apresentaçao())
# inspect(c1, methods=True) # Mostra os atributos e os metodos

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentaçao())

inspect(Funcionario)