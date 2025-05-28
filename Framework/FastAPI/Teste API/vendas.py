vendas = {
    1: {"item": "Coca-Cola Lata 350ml", "preço_unitario": 4, "quantidade_vendas": 5},
    2: {
        "item": "Guaraná Antarctica Garrafa 2L",
        "preço_unitario": 9.99,
        "quantidade_vendas": 5,
    },
    3: {"item": "Fanta Garrafa 600ml", "preço_unitario": 4.49, "quantidade_vendas": 5},
    4: {
        "item": "Guaraná Jesus Lata 350ml",
        "preço_unitario": 3.79,
        "quantidade_vendas": 5,
    },
}


def mostrar_venda(idvenda):
    venda_escolhida = vendas[idvenda]
    return f"Produto: {venda_escolhida['item']}<br>Preço Unitário: {venda_escolhida['preço_unitario']}<br>Quantidade de Vendas: {venda_escolhida['quantidade_vendas']}"


total_vendas = 0

for venda in vendas.values():
    total_vendas += venda["quantidade_vendas"] * venda["preço_unitario"]

total_vendas = f"R${total_vendas:.2f}"
