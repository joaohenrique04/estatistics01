import scipy


def calcula_assimetria(dados, var):
    ass = scipy.stats.skew(dados)

    print("Para", var, "a assimetria retornou:", end=" ")
    
    if ass > 1:
        print("Cauda à Direita", end = ' ')
    elif ass < -1:
        print("Cauda à Esquerda", end = ' ')
    else:
        print("Simétrica", end = ' ')
    print(ass)

def calcula_curtose(dados, var):
    curt = scipy.stats.kurtosis(dados)

    print("Para", var, "a curtose retornou:", end=" ")

    if curt > 1:
        print("Acima do Ponto de Normalidade", end = ' ')
    elif curt < -1:
        print("Abaixo do Ponto de Normalidade", end = ' ')
    else:
        print("Ponto de Normalidade", end = ' ')
    print(curt)

def ret_p_value(dados, var):
    
    p_v = scipy.stats.shapiro(dados).pvalue
    
    calcula_assimetria(dados, var)
    if p_v > 0.05:
        calcula_curtose(dados, var)
    
    return p_v

def linha():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")