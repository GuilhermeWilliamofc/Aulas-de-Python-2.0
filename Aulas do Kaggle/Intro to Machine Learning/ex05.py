import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# salvando a localização do banco de dados numa variavel
caminho_do_banco_de_dados_imobiliario = 'Aulas do Kaggle/Intro to Machine Learning/dados/AmesHousing.csv'

# o pandas vai ler os dados e organizar em um "DataFrame" que vai ter o nome da variavel
dados_de_iowa = pd.read_csv(caminho_do_banco_de_dados_imobiliario)

# vai printar somente as colunas do banco de dados de Melbourne
# print(dados_de_iowa.columns)

# por convenção o valor que queremos prever se chama "y", mas pode chamar do que você quiser
y = dados_de_iowa.SalePrice

# Features são as colunas (ou variáveis) que você dá como entrada para o modelo. São os fatores usados para prever algo.
features_de_iowa = ['Overall Qual', 'Overall Cond', 
    'Year Built', 'Year Remod/Add',
    'Gr Liv Area', 'Total Bsmt SF',
    '1st Flr SF', '2nd Flr SF',
    'Full Bath', 'Half Bath', 'Bedroom AbvGr',
    'Kitchen Qual', 'TotRms AbvGrd',
    'Garage Cars', 'Garage Area',
    'Fireplaces', 'Heating QC',
    'Exter Qual', 'Bsmt Qual', 'Neighborhood',
    'Lot Area', 'Condition 1', 'Condition 2']

# Convertendo as colunas object para números

# precisamos criar um codificador diferente para cada coluna object, Isso é necessário porque cada coluna tem suas próprias categorias, Se você usar o mesmo LabelEncoder pra todas, ele vai misturar as categorias e gerar resultados errados.

# Kitchen Qual
codificador1 = LabelEncoder()
dados_de_iowa['Kitchen Qual'] = codificador1.fit_transform(dados_de_iowa['Kitchen Qual'])

# Heating QC
codificador2 = LabelEncoder()
dados_de_iowa['Heating QC'] = codificador2.fit_transform(dados_de_iowa['Heating QC'])

# Exter Qual
codificador3 = LabelEncoder()
dados_de_iowa['Exter Qual'] = codificador3.fit_transform(dados_de_iowa['Exter Qual'])

# Bsmt Qual
codificador4 = LabelEncoder()
dados_de_iowa['Bsmt Qual'] = codificador4.fit_transform(dados_de_iowa['Bsmt Qual'])

# Neighborhood
codificador5 = LabelEncoder()
dados_de_iowa['Neighborhood'] = codificador5.fit_transform(dados_de_iowa['Neighborhood'])

# Condition 1
codificador6 = LabelEncoder()
dados_de_iowa['Condition 1'] = codificador6.fit_transform(dados_de_iowa['Condition 1'])

# Condition 2
codificador7 = LabelEncoder()
dados_de_iowa['Condition 2'] = codificador7.fit_transform(dados_de_iowa['Condition 2'])

# por convenção os dados que serão enviados para o modelo de IA se chamam "x"
x = dados_de_iowa[features_de_iowa]

# não tem no tutorial mas no caso de textos precisamos tratar os dados, o modelo lê somente números, então precisamos transformar números em texto, o .info() vai mostrar o tipo de dado, precisamos tratar todos os dados tipo "object"
# print(x.info())

# print(x.describe())
# print(x.head()) # serve para visualizar as primeiras linhas do banco de dados (DataFrame)

# vamos treinar o modelo ainda, mas primeiro precisamos separar os dados, também não tem no tutorial mas acho isso importante, não podemos entregar todos os dados para o modelo de IA, precisamos de alguns dados sem treino para calcular a precisão do modelo

# Obs: O Scikit-Learn separa 75% para treino e 25% para teste.

# Os dados são embaralhados antes da divisão (para evitar, por exemplo, se o dataset estiver ordenado por preço).

# O valor de teste pode ser ajustado: train_test_split(x, y, test_size=0.2, random_state=1) 

# (test_size=0.2 → 20% para teste, 80% para treino, random_state=1 → garante que a divisão seja sempre igual (reprodutível))

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

# Criar o modelo
# "Muitos modelos de machine learning permitem um certo grau de aleatoriedade no treinamento. Especificar um número para `random_state` garante que você obtenha os mesmos resultados em cada execução. Isso é considerado uma boa prática. Você pode usar qualquer número, e a qualidade do modelo não dependerá significativamente do valor exato que você escolher."
modelo_de_floresta = RandomForestRegressor(random_state = 1)

modelo_de_floresta.fit(x_treino, y_treino)

previsao_da_floresta = modelo_de_floresta.predict(x_teste)

resultado = mean_absolute_error(y_teste, previsao_da_floresta)
print("Segundo os testes, O modelo de Random Forest teve:")
print(f"Erro médio: ${resultado:.2f}")

# Perguntar ao usuário se ele quer guardar o modelo de IA (O modelo é guardado usando o pickle)
resposta = " "
while resposta not in "sn" or resposta == "" or resposta == "sn":
    try:
        resposta = (
            input("\033[33mDeseja Salvar o Modelo? [S/N]: \033[m").strip().lower()
        )
        if resposta not in "sn" or resposta == "" or resposta == "sn":
            print("\033[31mErro: Por favor, Digite somente S ou N!\033[m")
    except KeyboardInterrupt:
        print("")
        print("\033[31mErro: Por favor, Digite somente S ou N!\033[m")
    if resposta == "n":
        print("\033[31mO modelo não foi salvo!\033[m")
        break
    elif resposta == 's':
        # Salvando o modelo treinado em um arquivo .pkl
        with open("modelo_treinado.pkl", "wb") as arquivo:
            pickle.dump(modelo_de_floresta, arquivo)
        print("\033[32mO modelo foi salvo com sucesso!\033[m")
        break