# imports
import numpy as np
import statistics as sta
import banco

# sync = np.array([94, 84.9, 82.6, 69.5, 80.1, 79.6, 81.4, 77.8, 81.7, 78.8, 73.2, 87.9, 87.9, 93.5, 82.3, 79.3, 78.3, 71.6, 88.6, 74.6, 74.1, 80.6])
# asyncr = np.array([77.1, 71.7, 91, 72.2, 74.8, 85.1, 67.6, 69.9, 75.3, 71.7, 65.7, 72.6, 71.5, 78.2])

# busca no banco
syncAtual = banco.sync1 ## 22 dados
asyncAtual = banco.asyncr1 ## 14 dados

# média
x1 = syncAtual.mean()
x2 = asyncAtual.mean()

# mediana
me1 = np.median(syncAtual)
me2 = np.median(asyncAtual)

# quartil 1
sq1 = np.percentile(syncAtual, 25)
aq1 = np.percentile(asyncAtual, 25)

# quartil 3
sq3 = np.percentile(syncAtual, 75)
aq3 = np.percentile(asyncAtual, 75)

# moda
modaS = sta.multimode(syncAtual)
modaA = sta.multimode(asyncAtual)

# saídas
print("Iniciando...")

print("média sync:", x1)
print("média asyncr:", x2)
print("mediana sync:", me1)
print("mediana async:", me2)
print("sync quartil 1:", sq1)
print("sync quartil 3:", sq3)
print("async quartil 1:", aq1)
print("async quartil 3:", aq3)

print("moda sync:", modaS)
print("moda async:", modaA)