import scipy
import matplotlib.pyplot as plt
import math


def calcula_assimetria(dados, var):
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
    
    p_v = scipy.stats.shapiro(dados).pvalue
    
    calcula_assimetria(dados, var)
    if p_v > 0.05:
        calcula_curtose(dados, var)
    else:
        print("Hipótese nula desconsiderada.")
    
    return p_v

def hist(dados, title):
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
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")