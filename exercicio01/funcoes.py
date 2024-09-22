import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import math


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
    
    calcula_assimetria(dados, var)
    if p_v > 0.05:
        calcula_curtose(dados, var)
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

def linha():
    # imprime linha
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")