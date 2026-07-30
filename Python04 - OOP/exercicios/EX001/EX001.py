"""
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie tambem um metodo que permita ao funcionario se apresentar.
"""

from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentaçao(self):
        return f":slightly_smiling_face: Ola, sou [blue]{self.nome}[/] e "\
        f"sou {self.cargo} no setor {self.setor}. Na empresa curso em video."
    
c1 = Funcionario("Maria", "Administraçao", "Diretora")
print(c1.apresentaçao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentaçao())