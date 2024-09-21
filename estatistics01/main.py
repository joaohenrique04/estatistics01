# imports
import funcoes as fn
import scipy

# busca no banco
syncAtual = fn.buscaBanco(1)
asyncAtual = fn.buscaBanco(2)

p_valor_sync = scipy.stats.shapiro(syncAtual)
p_valor_async = scipy.stats.shapiro(asyncAtual)

# print("sync", p_valor_sync.pvalue)
# fn.compara_h0(p_valor_sync.pvalue)
# print("async", p_valor_async.pvalue)
# fn.compara_h0(p_valor_async.pvalue)

sync_assimetria = scipy.stats.skew(syncAtual)
async_assimetria = scipy.stats.skew(asyncAtual)

print("assimetria")
print (sync_assimetria)
print (async_assimetria)

sync_kurt = scipy.stats.kurtosis(syncAtual)
async_kurt = scipy.stats.kurtosis(asyncAtual)

print("curtose")
print(sync_kurt)
print(async_kurt)


"""""
AULA ANTERIOR ABAIXO
"""""
# operacoes
# fn.media(syncAtual)
# fn.media(asyncAtual)

# fn.linha()

# fn.mediana(syncAtual)
# fn.mediana(asyncAtual)

# fn.linha()

# fn.moda(syncAtual)
# fn.moda(asyncAtual)

# fn.linha()

# fn.percentil(syncAtual, 25)
# fn.percentil(asyncAtual, 25)

# fn.linha()

# fn.percentil(syncAtual, 75)
# fn.percentil(asyncAtual, 75)

# fn.linha()

# fn.amplitude(syncAtual)
# fn.amplitude(asyncAtual)

# fn.linha()

# fn.variancia(syncAtual, 0) # populacao
# fn.variancia(asyncAtual, 0)

# fn.linha()

# fn.variancia(syncAtual, 1) # amostra
# fn.variancia(asyncAtual, 1)

# fn.linha()

# fn.desvioPadrao(syncAtual, 0) # populacao
# fn.desvioPadrao(asyncAtual, 0)

# fn.linha()

# fn.desvioPadrao(syncAtual, 1) # amostra
# fn.desvioPadrao(asyncAtual, 1)