import pandas as pd

bd = pd.read_csv('iris.csv')

bd_setosa = bd[bd['Species'] == 'Iris-setosa']
bd_versicolor = bd[bd['Species'] == 'Iris-versicolor']
bd_virginica = bd[bd['Species'] == 'Iris-virginica']