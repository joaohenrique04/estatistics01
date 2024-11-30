from banco_dados import *
from numpy import *
from funcoes import *
from sklearn.linear_model import LinearRegression

# disp('label1', bd_cars["mpg"], 'label2', bd_cars["cyl"], 'title', 'data')

"""
ret_p_value(bd_cars["cyl"], 'cyl')
ret_p_value(bd_cars["disp"], 'disp')
ret_p_value(bd_cars["hp"], 'hp')
"""

"""
print(spearman(bd_cars["mpg"], bd_cars["cyl"]))
print(spearman(bd_cars["mpg"], bd_cars["disp"]))
print(spearman(bd_cars["mpg"], bd_cars["hp"]))


spearman_str(bd_cars["mpg"], bd_cars["cyl"])
spearman_str(bd_cars["mpg"], bd_cars["disp"])
spearman_str(bd_cars["mpg"], bd_cars["hp"])
"""
"""
X = bd_cars[['cyl', 'disp', 'hp']]
Y = bd_cars[['mpg']]

model = LinearRegression()

model.fit(X, Y)

print(f"Intercepts: {model.intercept_}")
print(f"Coeficientes: {model.coef_}")
print(f"R-squared: {model.score(X, Y)}")
"""
# ou seja...
# y1 = 34.18 - 1.22.x1 - 0.019.x2 - 0.015.x3