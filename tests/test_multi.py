# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    def test_multi(self):
        assert multi(3,4) == 12
        assert multi(10,2) == 20
        assert multi(-4, 5) == -20
        assert multi(-2,-6) == 12