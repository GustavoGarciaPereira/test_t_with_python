import pandas as pd

# Criando uma matriz utilizando o pandas
dados_clinicos = pd.DataFrame(
    [[1, 4, 5], [6, 3, 1]],
    columns=['Leve', 'Medio', 'Grave'],
    index=['Remedio', 'Placebo']
)

# Calculando as somas das linhas e colunas para frequências esperadas
soma_linhas = dados_clinicos.sum(axis=1)
soma_colunas = dados_clinicos.sum(axis=0)

# Imprimindo as somas para verificar
print(soma_linhas.values)
print(soma_colunas.values)

# Calculando o total geral dos dados
total_geral = dados_clinicos.sum().sum()
print(total_geral)

# Criando a matriz de frequência esperada
frequencias_esperadas = pd.DataFrame(
    [
        [
            (soma_linha * soma_coluna) / total_geral for soma_coluna in soma_colunas
        ]
        for soma_linha in soma_linhas
    ],
    columns=dados_clinicos.columns,
    index=dados_clinicos.index
)
print(frequencias_esperadas)

# Calculando a diferença entre as frequências esperadas e observadas
diferencas = dados_clinicos - frequencias_esperadas
print(diferencas)

# Calculando o valor do qui-quadrado
qui_quadrado_valores = (diferencas ** 2) / frequencias_esperadas
print(qui_quadrado_valores)

# Somando todos os valores para obter o qui-quadrado total
qui_quadrado_total = qui_quadrado_valores.sum().sum()
print(qui_quadrado_total)
