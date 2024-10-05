# imports
import funcoes as fn

banco1 = fn.buscaBanco(11)
banco2 = fn.buscaBanco(12)


fn.ret_p_value(banco1, 'antes')
fn.ret_p_value(banco2, 'depois')

fn.linha()
fn.levene(banco1, banco2)
fn.linha()

fn.ttest_rel(banco1, banco2)


# fn.hipotese2(banco1, banco2, banco3)
# fn.posthoc(banco1, banco2, banco3)

#fn.whitney(banco1, banco2)

# fn.anova_kruskal(banco1, banco2, banco3)
# fn.posthoc_no(banco1, banco2, banco3)