from banco_dados import *
from funcoes import *
import scipy
# Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species


# COMPRIMENTOS DE PÉTALA:

c_pet_setosa = round(bd_setosa["PetalLengthCm"].mean(), 2) ## 1.464 cm (3)
c_pet_versicolor = round(bd_versicolor["PetalLengthCm"].mean(),2) ## 4.26 cm (2)
c_pet_virginica = round(bd_virginica["PetalLengthCm"].mean(),2) ## 5.55 cm (1)

# print(c_pet_setosa, c_pet_versicolor, c_pet_virginica)

# DISTRIBUICAO

## Comprimento da Sépala
### Setosa
p_value_cs_setosa = ret_p_value(bd_setosa["SepalLengthCm"], 'Comprimento de Sépala da Setosa') ## 0.460
linha()
### Versicolor
p_value_cs_versicolor = ret_p_value(bd_versicolor["SepalLengthCm"], 'Comprimento de Sépala da Versicolor') ## 0.465
linha()
### Virginica
p_value_cs_virginica = ret_p_value(bd_virginica["SepalLengthCm"], 'Comprimento de Sépala da Virginica') ## 0.258
linha()

# AS 3 ESPECIES REJEITAM A HIPÓTESE NULA

print(p_value_cs_setosa, p_value_cs_versicolor, p_value_cs_virginica)