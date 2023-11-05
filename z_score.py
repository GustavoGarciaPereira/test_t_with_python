from statistics import stdev, mean
import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/classic-rock/classic-rock-song-list.csv"


dados_teste = [1,2,3,4,5,6]
dados_transformados = []


dados = pd.read_csv(url)
dados.hist()
dados = dados.head(30)

PlayCount = dados['PlayCount']

media = mean(PlayCount)
desvio_padrao = stdev(PlayCount)

# calcula o z-score
for i in PlayCount:
    dados_transformados.append((i-media)/desvio_padrao)

print(dados_transformados)

# # reconstroi os dados originais
# for i in dados_transformados:
#     print((desvio_padrao*i)+media)

# plt.hist(dados_transformados, bins=10)

# Exiba o histograma
plt.show()