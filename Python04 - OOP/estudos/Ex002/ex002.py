# Declaraçao de classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto (nome, idade)
    """
    def __init__(self, nome="vazio", idade=0): # Metodo Construtor
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade

        # Metodos de instancia
    def aniversario(self):
        self.idade  += 1
    
    def __str__(self): # Todo objeto ja tem um metodo str, que mostra o endereço na memoria. Mas podemos personalizar isso. Dunder method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos."
    
    def __getstate__(self): # Mostrar o estado
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaraçao de objetos
g1 = Gafanhoto("Maria", 17) 
g1.aniversario()

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()

g3 = Gafanhoto()

print(g1.__doc__) # Dunder Attribute

print(g1, g2, g3)

print(g1.__dict__) # Attribute, mostra o objeto em um dicionario
print(g1.__getstate__()) # Method, que tambem mostra o objeto em um dicionario
print(g1.__class__) # Attribute, mostra qual classe perecente o objeto