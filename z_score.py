from statistics import stdev, mean

dados_teste = [1,2,3,4,5,6]
dados_transformados = []


media = mean(dados_teste)
desvio_padrao = stdev(dados_teste)

# calcula o z-score
for i in dados_teste:
    dados_transformados.append((i-media)/desvio_padrao)

print(dados_transformados)

# reconstroi os dados originais
for i in dados_transformados:
    print((desvio_padrao*i)+media)