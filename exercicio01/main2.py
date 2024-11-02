from banco_dados import *
from funcoes import *
from numpy import *
from sklearn.linear_model import LinearRegression

# Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species

x = array_petal_length.reshape(-1, 1)
y = array_petal_width

modeloPet = LinearRegression()
modeloPet.fit(x, y)

print("petala:", modeloPet.score(x, y))


z = array_sepal_length.reshape(-1, 1)
k = array_sepal_width

modeloSep = LinearRegression()
modeloSep.fit(z, k)

print("sepala:", modeloSep.score(z, k))

# REGRESSAO
## SETOSA
### PETALA
# regressao(array_petal_length.reshape(-1, 1), array_petal_width)
### SEPALA
# regressao(array_sepal_length.reshape(-1, 1), array_sepal_width)
# ## VIRGINICA
# ### PETALA
# print("petala")
# regressao(array_petal_length.reshape(-1, 1), array_petal_width)
# ### SEPALA
# print("sepala")
# regressao(array_sepal_length.reshape(-1, 1), array_sepal_width)
# ## VERSICOLOR
# ### PETALA
# ret_p_value(bd_versicolor_petal, 'bd_versicolor_petal')
# correlacao(bd_versicolor_petal['PetalLengthCm'], bd_versicolor_petal['PetalWidthCm'])
# ### SEPALA
# ret_p_value(bd_versicolor_sepal, 'bd_versicolor_sepal')
# correlacao(bd_versicolor_sepal['SepalLengthCm'], bd_versicolor_sepal['SepalWidthCm'])






# NORMALIDADE
## SETOSA
### PETALA
# ret_p_value(bd_setosa_petal, 'bd_setosa_petal')
# correlacao(bd_setosa_petal['PetalLengthCm'], bd_setosa_petal['PetalWidthCm'])
### SEPALA
# ret_p_value(bd_setosa_sepal, 'bd_setosa_sepal')
# correlacao(bd_setosa_sepal['SepalLengthCm'], bd_setosa_sepal['SepalWidthCm'])
# ## VIRGINICA
# ### PETALA
# ret_p_value(bd_virginica_petal, 'bd_virginica_petal')
# correlacao(bd_virginica_petal['PetalLengthCm'], bd_virginica_petal['PetalWidthCm'])
# ### SEPALA
# ret_p_value(bd_virginica_sepal, 'bd_virginica_sepal')
# correlacao(bd_virginica_sepal['SepalLengthCm'], bd_virginica_sepal['SepalWidthCm'])
# ## VERSICOLOR
# ### PETALA
# ret_p_value(bd_versicolor_petal, 'bd_versicolor_petal')
# correlacao(bd_versicolor_petal['PetalLengthCm'], bd_versicolor_petal['PetalWidthCm'])
# ### SEPALA
# ret_p_value(bd_versicolor_sepal, 'bd_versicolor_sepal')
# correlacao(bd_versicolor_sepal['SepalLengthCm'], bd_versicolor_sepal['SepalWidthCm'])







# corr_setosa_petala = 
# corr_setosa_sepala = 

# corr_virginica_petala = 
# corr_virginica_sepala = 

# corr_versicolor_petala = 
# corr_versicolor_sepala = 

