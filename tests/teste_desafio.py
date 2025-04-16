from python import desafio

def test_calculo_simples():
    resultado = desafio.calcular_idade(2000, 1, 1, 2025, 1, 1)
    assert resultado["anos"] == 25
