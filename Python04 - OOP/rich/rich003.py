from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="center")
tabela.add_column("Preço", justify="center")

tabela.add_row("Lapis", "R$1,90", style="green")
tabela.add_row("Borracha", "R$5,00", style="blue")

print(tabela)