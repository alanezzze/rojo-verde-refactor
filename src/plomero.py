def calcular_visita(zona, trabajo_mismo_dia=False, es_fin_de_semana=False):
    if zona == "periférica":
        base = 12000
    else:
        base = 8000

    multiplicador = 1.0
    if es_fin_de_semana:
        multiplicador += 0.5
    if trabajo_mismo_dia:
        multiplicador += 0.5

    return base * multiplicador