from banco_dados import *
from funcoes import *
# Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species

# COMPRIMENTOS DE PÉTALA: (Q1)
"""""
c_pet_setosa = round(bd_setosa["PetalLengthCm"].mean(), 2) ## 1.464 cm (3)
c_pet_versicolor = round(bd_versicolor["PetalLengthCm"].mean(),2) ## 4.26 cm (2)
c_pet_virginica = round(bd_virginica["PetalLengthCm"].mean(),2) ## 5.55 cm (1)
"""""
# print(c_pet_setosa, c_pet_versicolor, c_pet_virginica)

# DISTRIBUICAO (Q3)

## Comprimento da Sépala
### Setosa
"""""
p_value_cs_setosa = ret_p_value(bd_setosa["SepalLengthCm"], 'Comprimento de Sépala da Setosa') ## 0.460
hist(bd_setosa["SepalLengthCm"], "SepalLengthCm - Setosa")
linha()
### Versicolor
p_value_cs_versicolor = ret_p_value(bd_versicolor["SepalLengthCm"], 'Comprimento de Sépala da Versicolor') ## 0.465
hist(bd_versicolor["SepalLengthCm"], "SepalLengthCm - Versicolor")
linha()
### Virginica
p_value_cs_virginica = ret_p_value(bd_virginica["SepalLengthCm"], 'Comprimento de Sépala da Virginica') ## 0.258
hist(bd_virginica["SepalLengthCm"], "SepalLengthCm - Virginica")
linha()

## Largura da Sépala
### Setosa
p_value_ls_setosa = ret_p_value(bd_setosa["SepalWidthCm"], 'Largura de Sépala da Setosa') ## 0.460
hist(bd_setosa["SepalWidthCm"], "SepalWidthCm - Setosa")
linha()
### Versicolor
p_value_ls_versicolor = ret_p_value(bd_versicolor["SepalWidthCm"], 'Largura de Sépala da Versicolor') ## 0.465
hist(bd_versicolor["SepalWidthCm"], "SepalWidthCm - Versicolor")
linha()
### Virginica
p_value_ls_virginica = ret_p_value(bd_virginica["SepalWidthCm"], 'Largura de Sépala da Virginica') ## 0.258
hist(bd_virginica["SepalWidthCm"], "SepalWidthCm - Virginica")
linha()

## Comprimento da Pétala
### Setosa
p_value_cp_setosa = ret_p_value(bd_setosa["PetalLengthCm"], 'Comprimento de Pétala da Setosa') ## 0.460
hist(bd_setosa["PetalLengthCm"], "PetalLengthCm - Setosa")
linha()
### Versicolor
p_value_cp_versicolor = ret_p_value(bd_versicolor["PetalLengthCm"], 'Comprimento de Pétala da Versicolor') ## 0.465
hist(bd_versicolor["PetalLengthCm"], "PetalLengthCm - Versicolor")
linha()
### Virginica
p_value_cp_virginica = ret_p_value(bd_virginica["PetalLengthCm"], 'Comprimento de Pétala da Virginica') ## 0.258
hist(bd_virginica["PetalLengthCm"], "PetalLengthCm - Virginica")
linha()

## Largura da Pétala
### Setosa
p_value_cp_setosa = ret_p_value(bd_setosa["PetalWidthCm"], 'Largura de Pétala da Setosa') ## 0.460
hist(bd_setosa["PetalWidthCm"], "PetalWidthCm - Setosa")
linha()
### Versicolor
p_value_cp_versicolor = ret_p_value(bd_versicolor["PetalWidthCm"], 'Largura de Pétala da Versicolor') ## 0.465
hist(bd_versicolor["PetalWidthCm"], "PetalWidthCm - Versicolor")
linha()
### Virginica
p_value_cp_virginica = ret_p_value(bd_virginica["PetalWidthCm"], 'Largura de Pétala da Virginica') ## 0.258
hist(bd_virginica["PetalWidthCm"], "PetalWidthCm - Virginica")
linha()

## USADOS PARA GERAR NOVAMENTE OS HISTOGRAMAS QUE A FUNCAO AUTOMATICA NAO RESOLVERAM
# hist_bins(bd_setosa["PetalWidthCm"], "PetalWidthCm - Setosa", 6)
# hist_bins(bd_virginica["PetalWidthCm"], "PetalWidthCm - Virginica", 6)
"""""

# GRAFICO DE DISPERSAO (Q2)
# COMPRIMENTO DE PETALA VS COMPRIMENTO DE SEPALA
## SETOSA
"""""
disp('Sepal_Length_Cm', bd_setosa['PetalLengthCm'], 'Petal_Length_Cm', bd_setosa['SepalLengthCm'], "Comprimento de Sépala x Pétala", "Iris-setosa")
## VERSICOLOR
disp('Sepal_Length_Cm', bd_versicolor['PetalLengthCm'], 'Petal_Length_Cm', bd_versicolor['SepalLengthCm'], "Comprimento de Sépala x Pétala", "Iris-versicolor")
## VIRGINICA
disp('Sepal_Length_Cm', bd_virginica['PetalLengthCm'], 'Petal_Length_Cm', bd_virginica['SepalLengthCm'], "Comprimento de Sépala x Pétala", "Iris-virginica")
"""""