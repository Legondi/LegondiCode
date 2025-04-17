import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../python")))

from desafio import calcular_idade

def test_calculo_simples():
    resultado = calcular_idade(2000, 1, 1, 2025, 1, 1)
    assert resultado["anos"] == 25
