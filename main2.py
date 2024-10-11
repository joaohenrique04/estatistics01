# imports
import funcoes as fn

banco1 = fn.buscaBanco(17)
banco2 = fn.buscaBanco(18)
banco3 = fn.buscaBanco(19)


# fn.ret_p_value(banco1, 'dieta a')
# fn.ret_p_value(banco2, 'dieta b')
# fn.ret_p_value(banco3, 'dieta c')


# fn.linha()
# fn.levene(banco1, banco2, banco3)
# fn.linha()

fn.hipotese2(banco1, banco2, banco3)

fn.posthoc(banco1, banco2, banco3)
# fn.var_dif(banco1, banco2)
# fn.hipotese1(banco1, banco2)
# fn.ttest_rel(banco1, banco2)


# fn.hipotese2(banco1, banco2, banco3)
# fn.posthoc(banco1, banco2, banco3)

#fn.whitney(banco1, banco2)

# fn.anova_kruskal(banco1, banco2, banco3)
# fn.posthoc_no(banco1, banco2, banco3)
