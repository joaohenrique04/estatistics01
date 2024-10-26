import banco
import numpy as np
import scipy
import statistics as sta
import scikit_posthocs as sp

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
        case 3:
            return banco.only_breast
        case 4:
            return banco.only_formula
        case 5:
            return banco.both
        case 6:
            return banco.test_team
        case 7:
            return banco.developer_team
        case 8:
            return banco.youtube
        case 9:
            return banco.instagram
        case 10:
            return banco.facebook
        case 11:
            return banco.before_diet
        case 12:
            return banco.after_diet
        case 13:
            return banco.grupo_a
        case 14:
            return banco.grupo_b
        case 15:
            return banco.especie_x
        case 16:
            return banco.especie_y
        case 17:
            return banco.dieta_a
        case 18:
            return banco.dieta_b
        case 19:
            return banco.dieta_c
        case 20:
            return banco.reg
        case 21:
            return banco.reg2

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

def compara_h0(x):
    if x < 0.05:
        print("H0 rejeitada!")
    else:
        print("H0 não foi rejeitada")


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
    # shapiro
    # retorna o p_value e ja retorna informaoes de assimetria e curtose
    p_v = scipy.stats.shapiro(dados).pvalue
    print("p_value shapiro", p_v)
    #calcula_assimetria(dados, var)
    if p_v > 0.05:
        #calcula_curtose(dados, var)
        print("Normal")
    else:
        print("Hipótese nula desconsiderada.")
        print("Assimetrico")
    
    return p_v

def levene(* banco):
    #H0 = VARIANCIAS IGUAIS
    #H1 = VARIANCIAS DIFERENTES
    test_stat_var, p_value_var = scipy.stats.levene(* banco)
    print("p value levene: ", p_value_var)
    if p_value_var < 0.05:
        print("Rejeita hipotese nula")
    else:
        print("Nao pode rejeitar a hipotese, variancias sao iguais")

def hipotese1(banco1, banco2):
    # HIPOTESES NORMAIS
    # MESMA VARIANCIA
    ttest, p_value = scipy.stats.ttest_ind(banco1, banco2)
    print("p_value ttest", p_value)

    # divide o p valor por 2 pois é um teste de somente um lado
    if p_value/2 < 0.05:
        print("hipotese nula rejeitada")
    else:
        print("hipotese nula aceita")

    #H0 = MEDIAS IGUAIS
    #H1 = MEDIAS DIFERENTES

def var_dif(banco1, banco2):
    # HIPOTESES NORMAIS
    # MESMA VARIANCIA
    ttest, p_value = scipy.stats.ttest_ind(banco1, banco2, equal_var=False)
    print("p_value ttest", p_value)

    # divide o p valor por 2 pois é um teste de somente um lado
    if p_value/2 < 0.05:
        print("hipotese nula rejeitada")
    else:
        print("hipotese nula aceita")

    #H0 = MEDIAS IGUAIS
    #H1 = MEDIAS DIFERENTES
    
def hipotese2(banco1, banco2, banco3):
    # TESTE DE ANOVA
    # HIPOTESES NORMAIS
    # MESMA VARIANCIA
    anova, p_value = scipy.stats.f_oneway(banco1, banco2, banco3)

    print("p_value anova", p_value)

    # divide o p valor por 2 pois é um teste de somente um lado
    if p_value < 0.05:
        print("hipotese nula rejeitada")
    else:
        print("hipotese nula aceita")

    #H0 = MEDIAS IGUAIS
    #H1 = PELO MENOS UMA DIFERENTE

def posthoc(banco1, banco2, banco3):
    group_names = ['dieta a', 'dieta b', 'dieta c']
    posthoc_df = sp.posthoc_ttest([banco1, banco2, banco3], equal_var = True, p_adjust="bonferroni")

    posthoc_df.columns = group_names
    posthoc_df.index = group_names

    print(posthoc_df)

def whitney(banco1, banco2):
    # H0 MEDIAS IGUAIS
    # H1 MEDIAS DIFERENTES
    utest, p_value = scipy.stats.mannwhitneyu(banco1, banco2, alternative = 'two-sided')
    print('p_value whitney', p_value)
    if p_value < 0.05:
        print("Descarta-se a hipotese nula (medias diferentes)")
    else:
        print("Nao se pode descartar a hipotese nula") 

def anova_kruskal(banco1, banco2, banco3):

    f, p_value = scipy.stats.kruskal(banco1, banco2, banco3)
    print('p_value kruskal', p_value)

    if p_value < 0.05:
        print("rejeita hipotese nula")
    else:
        print("nao se descarta a hipotese nula")

def whitney_no(banco1, banco2, banco3):
    # H0 MEDIAS IGUAIS
    # H1 MEDIAS DIFERENTES
    utest, p_value = scipy.stats.mannwhitney(banco1, banco2, banco3, alternative = 'two-sided')
    print('p_value whitney', p_value)
    if p_value < 0.05:
        print("Descarta-se a hipotese nula (medias diferentes)")
    else:
        print("Nao se pode descartar a hipotese nula") 

def posthoc_no(banco1, banco2, banco3):
    group_names = ['yt', 'insta', 'face']
    posthoc_df = sp.posthoc_ttest([banco1, banco2, banco3], equal_var = False, p_adjust="bonferroni")

    posthoc_df.columns = group_names
    posthoc_df.index = group_names

    print(posthoc_df)

def ttest_rel(banco1, banco2):
    test_stat, p_value_paired = scipy.stats.ttest_rel(banco1, banco2)
    print(f"p_value paired {p_value_paired:.10f}")
    if p_value_paired < 0.05:
        print("rejeita hipotese nula")
    else:
        print("impossivel rejeitar")