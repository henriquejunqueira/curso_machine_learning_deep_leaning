# -*- coding: utf-8 -*-
"""Introdução a Machine Learning e Classificação - 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HgeXSv-cbAno9NtsRENqGvUqAS1oq9U4
"""

# features/características (1 sim, 0 não):
# pelo longo?
# perna curta?
# faz auau?

porco1 = [0, 1, 0] # porco1 = [pelo_longo, perna_curta, faz_auau]
porco2 = [0, 1, 1] # esse porco é especial então faz "auau"
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

# classificação
# 1 => porco, 0 => cachorro
# dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
#classe = [1, 1, 1, 0, 0, 0] # labels / etiqueta
treino_y = [1, 1, 1, 0, 0, 0] # labels / etiqueta

#f(x) = y # x => dados (treino_x), y => classe (treino_y)

from sklearn.svm import LinearSVC

model = LinearSVC()
#model.fit(dados, classes)
model.fit(treino_x, treino_y)

animal_misterioso = [1, 1, 1]
model.predict([animal_misterioso]) # prevê o resultado

misterio1 = [1, 1, 1]
misterio2 = [1, 1, 0]
misterio3 = [0, 1, 1]

# testes = [misterio1, misterio2, misterio3]
teste_x = [misterio1, misterio2, misterio3]
#testes_classes = [0, 1, 1]
teste_y = [0, 1, 1]

#previsoes = model.predict(teste)
previsoes = model.predict(teste_x) # prevê o resultado

#previsoes # isso é um array
#testes_classes # isso é uma lista
#previsoes == testes_classes # comparação de elementos que retorna um array com True ou False
#corretos = (previsoes == testes_classes).sum()
corretos = (previsoes == teste_y).sum() # soma o número de elementos verdadeiro no array
total = len(teste_x)
taxa_de_acerto = corretos / total
print("Taxa de acerto %.2f " % (taxa_de_acerto * 100)) # multiplica por 100 pra dar a porcentagem de acerto

from sklearn.metrics import accuracy_score

# taxa_de_acerto = accuracy_score(testes_classes, previsoes)
taxa_de_acerto = accuracy_score(teste_y, previsoes)
print("Taxa de acerto %.2f " % (taxa_de_acerto * 100))

