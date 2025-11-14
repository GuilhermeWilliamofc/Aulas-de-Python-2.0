import pickle
import pandas as pd

# Caminho do arquivo do modelo
caminho_modelo = "modelo_treinado.pkl"

# Carregar o modelo salvo
with open(caminho_modelo, "rb") as arquivo:
    modelo_carregado = pickle.load(arquivo)

print("✅ Modelo carregado com sucesso!")

# Criar um pequeno exemplo de entrada (usando as mesmas colunas do treinamento)
exemplo = pd.DataFrame({
    'Overall Qual': [7],
    'Overall Cond': [5],
    'Year Built': [2005],
    'Year Remod/Add': [2007],
    'Gr Liv Area': [1800],
    'Total Bsmt SF': [900],
    '1st Flr SF': [900],
    '2nd Flr SF': [900],
    'Full Bath': [2],
    'Half Bath': [1],
    'Bedroom AbvGr': [3],
    'Kitchen Qual': [3],  # deve ser um número (LabelEncoded)
    'TotRms AbvGrd': [7],
    'Garage Cars': [2],
    'Garage Area': [480],
    'Fireplaces': [1],
    'Heating QC': [3],
    'Exter Qual': [3],
    'Bsmt Qual': [3],
    'Neighborhood': [5],
    'Lot Area': [8000],
    'Condition 1': [2],
    'Condition 2': [2]
})

# Fazer a previsão
previsao = modelo_carregado.predict(exemplo)
print(f"💰 Valor previsto da casa: ${previsao[0]:.2f}")
