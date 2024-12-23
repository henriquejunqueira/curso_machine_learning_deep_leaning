# -*- coding: utf-8 -*-
"""Introdução a Machine Learning Classificação - 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gzV0iIakb82hABJYIQtsp62PldG6TmO8
"""

import pandas as pd

uri = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
#pd.read_csv(uri) # Lê o arquivo CSV
dados = pd.read_csv(uri) # Lê o arquivo CSV e atribui em dados
dados.head() # mostra as 5 primeiras linhas do arquivo

# Renomeando nome das colunas com pandas
mapa = {
    "home" : "principal",
    "how_it_works" : "como_funciona",
    "contact" : "contato",
    "bought" : "comprou"
}

dados = dados.rename(columns = mapa)

x = dados[["principal", "como_funciona", "contato"]] # define quais colunas serão listadas
x.head()
y = dados["comprou"]
y.head()

dados.shape # exibe a quantidade de elementos

treino_x = x[:75] # pega até o elemento 75, ou seja do 0 até o 74
treino_y = y[:75] # pega até o elemento 75, ou seja do 0 até o 74

teste_x = x[75:] # à partir do elemento 75, ou seja, do 75 em diante
teste_y = y[75:] # à partir do elemento 75, ou seja, do 75 em diante
#teste_y.shape

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

# treinando o modelo

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100 # acuracia é a taxa de acerto
print("A acurácia foi %.2f%%" % acuracia)

"""# Usando a biblioteca para separar treino e teste"""

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

SEED = 20 # define um número inicial pro algoritmo de geração de números aleatórios

# o train_test_split separa o treino de forma randômica, por isso é necessário o SEED
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state = SEED, test_size = 0.25)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

# treino_y.value_counts() # retorna a contagem dos valores
teste_y.value_counts()

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

SEED = 20 # define um número inicial pro algoritmo de geração de números aleatórios

# o train_test_split separa o treino de forma randômica, por isso é necessário o SEED
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, random_state = SEED, test_size = 0.25, stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)

treino_y.value_counts()

teste_y.value_counts()