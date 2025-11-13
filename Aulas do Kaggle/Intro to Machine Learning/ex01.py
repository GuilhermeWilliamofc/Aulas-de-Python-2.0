import pandas as pd

# salvando a localização do banco de dados numa variavel
caminho_do_banco_de_dados_imobiliario = 'Aulas do Kaggle/Intro to Machine Learning/dados/melb_data.csv'

# o pandas vai ler os dados e organizar em um "DataFrame" que vai ter o nome da variavel
dados_de_melbourne = pd.read_csv(caminho_do_banco_de_dados_imobiliario)

# vai printar o banco de dados de Melbourne
print(dados_de_melbourne.describe())