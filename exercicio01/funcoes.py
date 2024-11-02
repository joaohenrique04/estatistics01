import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression


def calcula_assimetria(dados, var):
    # retorna informacao de assimetria
    ass = scipy.stats.skew(dados)

    print("Para", var, "a assimetria retornou:", end=" ")
    
    if ass > 0.5:
        print("Cauda à Direita", end = ' ')
    elif ass < -0.5:
        print("Cauda à Esquerda", end = ' ')
    else:
        print("Simétrica", end = ' ')
    print(round(ass, 2))

def calcula_curtose(dados, var):
    # retorna informacao de curtose
    curt = scipy.stats.kurtosis(dados)

    print("Para", var, "a curtose retornou:", end=" ")

    if curt > 0.5:
        print("Acima do Ponto de Normalidade", end = ' ')
    elif curt < -0.5:
        print("Abaixo do Ponto de Normalidade", end = ' ')
    else:
        print("Ponto de Normalidade", end = ' ')
    print(round(curt,2))

def ret_p_value(dados, var):
    # retorna o p_value e ja retorna informaoes de assimetria e curtose
    p_v = scipy.stats.shapiro(dados).pvalue
    
    #calcula_assimetria(dados, var)
    if p_v > 0.05:
        #calcula_curtose(dados, var)
        print("Hipótese nula nao é desconsiderada.")
    else:
        print("Hipótese nula desconsiderada.")
    
    return p_v

def disp(label1, dados1, label2, dados2, title, data):
    # grafico de dispersao
    # Cria um DataFrame com os dados a serem plotados
    dados = pd.DataFrame({label1: dados1, label2: dados2})

    # Cria o gráfico de dispersão
    sns.scatterplot(data=dados, x=label1, y=label2, color='blue', label=data)

    # Configurações do gráfico
    plt.title(title)
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.legend()
    plt.show()

def hist(dados, title):
    # histograma
    v_min = min(dados)
    v_max = max(dados)
    num_dados = len(dados)

    v_bins = math.ceil(math.log2(num_dados) + 1)

    plt.hist(dados, bins=v_bins, range=(v_min, v_max), color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.show()

def hist_bins(dados, title, p_bins):
    # histograma com bins variavel
    v_min = min(dados)
    v_max = max(dados)
    num_dados = len(dados)

    #v_bins = math.ceil(math.log2(num_dados) + 1)
    v_bins = p_bins

    plt.hist(dados, bins=p_bins, range=(v_min, v_max), color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel("Valor")
    plt.ylabel("Frequência")
    plt.show()

def desviopadrao(dados, ddof):
    # calcula desvio padrao
    # 0 populacional / 1 amostra

    data = np.std(dados, ddof=ddof)
    data = round(data, 2) ## arredondar
    return (data)

def correlacao(col1, col2):
    # usado quando é normal
    cor = np.corrcoef(col1, col2)[0, 1]
    print(f'Coeficiente de correlação: {cor}')


def regressao(col1, col2):
    model = LinearRegression()
    model.fit(col1, col2)
    print('Coeficiente (A):', model.coef_)
    print('Intercept (B):', model.intercept_)

def calcular_ssr(y_true, y_pred):
    """
    Calcula a Soma dos Quadrados da Regressão (SSR).

    Parâmetros:
    y_true -- array com os valores verdadeiros (observados)
    y_pred -- array com as previsões do modelo

    Retorna:
    SSR -- a Soma dos Quadrados da Regressão
    """
    # Calcular a média dos valores verdadeiros
    media_y = np.mean(y_true)

    # Calcular o SSR
    ssr = np.sum((y_pred - media_y) ** 2)

    return ssr

def linha():
    # imprime linha
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")