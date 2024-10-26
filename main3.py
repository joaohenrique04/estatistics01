# imports
import funcoes as fn
import numpy as np
from sklearn.linear_model import LinearRegression

banco1 = fn.buscaBanco(20)
banco2 = fn.buscaBanco(21)

model = LinearRegression()
model.fit(banco1, banco2)

# r_sq = model.score(banco1, banco2) ## 71% (85% pra cima é uma boa acurácia)
# print(r_sq)

# print('coeficiente', model.coef_)   # ->> VALOR QUE MULTIPLICA O B
# print('termo independente', model.intercept_)   # ->> VALOR QUE FICA SOZINHO


banco2_pred = model.predict(banco1)   # ->> Y CALCULADOS DE MANEIRA PRATICA (SUBTRAIR ISSO DO Y ORIGINAL DÁ O ERRO)


## CALCULO DO SSR
# 1. SUBTRAIR O BANCO_PRED DO BANCO
# 2. ELEVAR O QUADRADO COM np.square
# 3. USAR O SUM
print(sum(np.square(banco2_pred-banco2)))

### CALCULAR REGRESSAO:
## TERMO INDEPENDETE + COEF. * X => Y