class Loja:
    
    taxa = 1.15

    def __init__(self, nome_loja: str, nome_produto: str, valor: float) -> None:
        self.nome_loja = nome_loja
        self.nome_do_produto = nome_produto
        self.valor_produto_bruto = valor

    def consultar_valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'Valor do Produto na {self.nome_loja} ({self.nome_do_produto}): R${valor_produto:.2f}')

    @classmethod
    def editar_taxa_do_produto(cls, taxa_nova: float):
        cls.taxa = taxa_nova

loja_praia = Loja('Loja Praia','Prancha', 30.50)
loja_shopping = Loja('Loja Shopping','Bolsa', 10.39)
loja_44 = Loja('Loja 44','Roupa', 20.33)

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_44.consultar_valor_do_produto()

loja_praia.editar_taxa_do_produto(1.35)
print('\033[33mNova taxa: 1.15 ----> 1.35\033[m')

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_44.consultar_valor_do_produto()
