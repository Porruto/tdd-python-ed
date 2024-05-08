# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    def test_div(self):
        assert div(5,5) == 1
        assert div(2,4) == 0.5
        assert div(8,4) == 2
        assert div(10,1) == 10