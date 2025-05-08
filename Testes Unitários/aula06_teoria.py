def desconto_porcento() -> float:
    return 0.10

def calcular_desconto(preco: float) -> float:
    desconto = desconto_porcento()
    return preco - (preco * desconto)
