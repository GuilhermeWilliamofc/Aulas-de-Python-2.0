import pandas as pd

# salvando a localização do banco de dados numa variavel
caminho_do_banco_de_dados_imobiliario = 'Aulas do Kaggle/Intro to Machine Learning/dados/AmesHousing.csv'

# o pandas vai ler os dados e organizar em um "DataFrame" que vai ter o nome da variavel
dados_de_iowa = pd.read_csv(caminho_do_banco_de_dados_imobiliario)

# vai printar somente as colunas do banco de dados de Melbourne
print(dados_de_iowa.columns)

""" 
Segundo o Kaggle:

Os dados de Melbourne têm alguns valores ausentes (algumas casas para as quais algumas variáveis não foram registradas).

Aprenderemos a lidar com valores ausentes em um tutorial posterior.  

Seus dados de Iowa não têm valores ausentes nas colunas que você usa. 

Portanto, vamos escolher a opção mais simples por enquanto e excluir as casas dos nossos dados. 

Não se preocupe muito com isso por enquanto

"melbourne_data = melbourne_data.dropna(axis=0)"
dropna exclui valores ausentes (pense em "na" como “not available”)
"""

dados_de_iowa = dados_de_iowa.dropna(axis = 0)

print(dados_de_iowa.columns)