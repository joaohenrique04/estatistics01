from banco_dados import *
from numpy import *
from funcoes import *
from sklearn.linear_model import LinearRegression

# 1. Existe relação entre o número de quartos (RM) e o valor médio das casas (MEDV) no Conjunto de Dados Boston Housing?
"""
# disp(label1, dados1, label2, dados2, title, data)
# disp('nro de quartos', bd_house["rm"], 'vlr_medio', bd_house["medv"], 'Correlação', 'data')

# ret_p_value(bd_house["rm"], 'nro de quartos')
# ret_p_value(bd_house["medv"], 'valor medio')

# spearman_str(bd_house["rm"], bd_house["medv"])

# X = np.array(bd_house['rm']).reshape(-1, 1)
# y = bd_house['medv']
"""
# 2. É possível prever o valor médio das casas (MEDV) com base apenas no número médio de quartos por residência (RM)?
"""
# Regressão Linear
model = LinearRegression()
model.fit(X, y)

# Coeficiente de Determinação (R²)
# r_squared = model.score(X, y)

# print(f"Coeficiente R²: {r_squared}")
# print(f"Coeficiente da regressão (inclinação): {model.coef_[0]}")
# print(f"Intercepto: {model.intercept_}")
"""
# 3. Como a taxa de criminalidade (CRIM), o número médio de quartos (RM) e a idade das propriedades (AGE) afetam coletivamente o valor médio das casas (MEDV)
"""
# print(ret_p_value(bd_house["crim"], 'criminalidade'))
# print(ret_p_value(bd_house["rm"], 'nro de quartos'))
# print(ret_p_value(bd_house["age"], 'idade'))

# spearman_str(bd_house["crim"], bd_house["medv"])
# spearman_str(bd_house["age"], bd_house["medv"])
# spearman_str(bd_house["rm"], bd_house["medv"])

# X = bd_house[['crim', 'rm', 'age']]
# Y = bd_house[['medv']]

# model = LinearRegression()

# model.fit(X, Y)

# print(f"Intercepts: {model.intercept_}")
# print(f"Coeficientes: {model.coef_}")
# print(f"R-squared: {model.score(X, Y)}")
"""
# 4. Qual é o impacto combinado de variáveis como a proporção de terrenos residenciais destinados a grandes lotes (ZN), a distância para os centros de emprego (DIS) e a razão aluno-professor (PTRATIO) sobre os preços das casas (MEDV)?
"""
# ret_p_value(bd_house["zn"], 'zn')
# ret_p_value(bd_house["dis"], 'dis')
# ret_p_value(bd_house["ptratio"], 'ptratio')

# spearman_str(bd_house["zn"], bd_house["medv"])
# spearman_str(bd_house["dis"], bd_house["medv"])
# spearman_str(bd_house["ptratio"], bd_house["medv"])

# X = bd_house[['zn', 'dis', 'ptratio']]
# Y = bd_house[['medv']]

# model = LinearRegression()

# model.fit(X, Y)

# print(f"Intercepts: {model.intercept_}")
# print(f"Coeficientes: {model.coef_}")
# print(f"R-squared: {model.score(X, Y)}")
"""
# 5. Dado que o conjunto de dados inclui várias variáveis como CRIM, INDUS, NOX e AGE, você pode construir um modelo de regressão para prever o preço das casas (MEDV)?
"""
# ret_p_value(bd_house["crim"], 'crim')
# ret_p_value(bd_house["indus"], 'indus')
# ret_p_value(bd_house["nox"], 'nox')
# ret_p_value(bd_house["age"], 'age')

# spearman_str(bd_house["crim"], bd_house["medv"])
# spearman_str(bd_house["indus"], bd_house["medv"])
# spearman_str(bd_house["nox"], bd_house["medv"])
# spearman_str(bd_house["age"], bd_house["medv"])

# X = bd_house[['crim', 'indus', 'nox', 'age']]
# Y = bd_house[['medv']]

# model = LinearRegression()

# model.fit(X, Y)

# print(f"Intercepts: {model.intercept_}")
# print(f"Coeficientes: {model.coef_}")
# print(f"R-squared: {model.score(X, Y)}")
"""