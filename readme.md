# Testes t de Student em Python

Este projeto oferece implementações em Python para realizar testes t de Student, que são úteis para avaliar a significância estatística entre diferentes conjuntos de dados ou entre um conjunto de dados e uma média de referência.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)

## Instalação

Este projeto não requer instalação, basta baixar o arquivo `main.py` do repositório e você está pronto para começar.

```bash
# Clone o repositório
git clone https://github.com/GustavoGarciaPereira/test_t_with_python.git
```


## uso
```bash
# Importe o script
import testes_t

# Seus dados
lista_A = [1,2,3,4,5,6]
lista_B = [1,2,3,4,5,6]

# Execute o teste t para amostras independentes
t_independente = testes_t.t_independente(lista_A, lista_B)
print(t_independente)
```



- [ ] estudar como calcular o p-valor
- [ ] estudar efeito