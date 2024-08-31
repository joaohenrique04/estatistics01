# imports
import numpy as np
import statistics as sta
import banco
import medidas1 as m1

def linha():
    print("=-=-=-=-=-=-=-=-=-=-=-=")


# busca no banco
syncAtual = banco.sync1 ## 22 dados
asyncAtual = banco.asyncr1 ## 14 dados

# maximo e minimo
maxS = max(syncAtual)
minS = min(syncAtual)

# amplitude
ampS = syncAtual.ptp()
ampA = asyncAtual.ptp()

# amplitude interquartil
iqrS = m1.sq3 - m1.sq1
iqrA = m1.aq3 - m1.aq1

# variancia
varS = syncAtual.var(ddof=1)
varA = asyncAtual.var(ddof=1)

# desvio padrao
sS = syncAtual.std(ddof=1)
sA = asyncAtual.std(ddof=1)

# saídas
print("Iniciando...")
linha()
print("maxS", maxS)
print("minS", minS)
linha()
print("amplit sync", ampS)
print("amplit async", ampA)
linha()
print("amplit sync interquartil", iqrS)
print("amplit async interquartil", iqrA)
linha()
print("variancia sync", varS)
print("variancia async", varA)
linha()
print("desvio p sync", sS)
print("desvio p async", sA)