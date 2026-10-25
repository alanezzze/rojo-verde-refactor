from src.plomero import calcular_visita

def test_zona_centrica_dia_de_semana_sin_trabajo_mismo_dia():
    assert calcular_visita("céntrica", trabajo_mismo_dia=False, es_fin_de_semana=False) == 8000

def test_zona_periferica_dia_de_semana_sin_trabajo_mismo_dia():
    assert calcular_visita("periférica", trabajo_mismo_dia=False, es_fin_de_semana=False) == 12000

def test_zona_centrica_fin_de_semana_sin_trabajo_mismo_dia():
    assert calcular_visita("céntrica", trabajo_mismo_dia=False, es_fin_de_semana=True) == 12000