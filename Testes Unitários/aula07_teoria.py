def desconto_porcento(valor_inicial) -> float:
    return 0.10 * valor_inicial

def calcular_desconto(preco: float) -> float:
    desconto = desconto_porcento(0.9)
    return preco - (preco * desconto)
