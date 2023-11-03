from statistics import mean, variance, stdev
from math import sqrt
lista_A = [1,2,3,4,5,6]
lista_B = [1,2,3,4,5,6]


mediaA = mean(lista_A)
mediaB = mean(lista_B)

varianzaA = variance(lista_A)
varianzaB = variance(lista_B)

nA = len(lista_A)
nB = len(lista_B)


t_independente = (mediaA - mediaB)/(sqrt((varianzaA/nA)+(varianzaB/nB)))

print(t_independente)

#==========================================================================

antes = [1,2,3,4,5,6]
depois = [1,2,3,4,5,6]

resultado = []
for i in range(len(antes)):
    resultado.append(antes[i] - depois[i])
    
delta = mean(resultado)
dp_delta = stdev(resultado)
n = len(depois)

t_pareado = delta/(dp_delta/sqrt(n))



#===========================================================================
amostra = [1,2,3,4,5,6]
m_referencia = 12

dp_amostra = stdev(amostra)
n = len(amostra)
t_para_uma_amostra = (mean(amostra) - m_referencia)/(dp_amostra/sqrt(n))