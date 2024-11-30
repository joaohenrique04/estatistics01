import pandas as pd
from numpy import *

bd = pd.read_csv('iris.csv')

bd_setosa = bd[bd['Species'] == 'Iris-setosa']
bd_versicolor = bd[bd['Species'] == 'Iris-versicolor']
bd_virginica = bd[bd['Species'] == 'Iris-virginica']

bd_setosa_sepal = bd_setosa[['Id', 'SepalLengthCm', 'SepalWidthCm']]
bd_setosa_petal = bd_setosa[['Id', 'PetalLengthCm', 'PetalWidthCm']]

bd_versicolor_sepal = bd_versicolor[['Id', 'SepalLengthCm', 'SepalWidthCm']]
bd_versicolor_petal = bd_versicolor[['Id', 'PetalLengthCm', 'PetalWidthCm']]

bd_virginica_sepal = bd_virginica[['Id', 'SepalLengthCm', 'SepalWidthCm']]
bd_virginica_petal = bd_virginica[['Id', 'PetalLengthCm', 'PetalWidthCm']]

array_petal_length = bd_virginica['PetalLengthCm'].to_numpy()
array_petal_width = bd_virginica['PetalWidthCm'].to_numpy()

array_sepal_length = bd_virginica['SepalLengthCm'].to_numpy()
array_sepal_width = bd_virginica['SepalWidthCm'].to_numpy()

bd_cars = pd.read_csv('mtcars.csv')
bd_cerveja = pd.read_csv('consumo_cerveja.csv')

bd_house = pd.read_csv('BostonHousing.csv')