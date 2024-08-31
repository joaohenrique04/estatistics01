import banco
import numpy as np
import statistics as sta

# funcao controle de impressao
def linha():
    print("=-=-=-=-=-=-=-=-=-=-=-=")

# funcao de busca de valores do banco
def buscaBanco(id):
    match id:
        case 1:
            return banco.sync1
        case 2:
            return banco.asyncr1

def media(banco):
    var = banco.mean()

    print("Média:", var)

    return var

def mediana(banco):
    var = np.median(banco)

    print("Mediana:", var)

    return var

def moda(banco):
    var = sta.multimode(banco)

    print(var)

    print("Moda:", var)

    return var

def percentil(banco, pct):
    var = np.percentile(banco, pct)

    print(f"Percentil de {pct}:", var)

    return var

def amplitude(banco):
    # forma antiga: var = banco.ptp() 
    var = np.ptp(banco)

    print("Amplitude:", var)

    return var

def variancia(banco, tipo):
    var = banco.var(ddof=tipo)

    if tipo == 0:
        tp = "População"
    else:
        tp = "Amostra"

    print(f"Variância {tp}:", var)

    return var

def desvioPadrao(banco, tipo):
    var = banco.std(ddof=tipo)

    if tipo == 0:
        tp = "População"
    else:
        tp = "Amostra"

    print(f"Desvio Padrão {tp}:", var)

    return var

