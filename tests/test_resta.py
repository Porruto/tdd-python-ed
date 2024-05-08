# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    def test_resta(self):
        assert resta(10,5) == 5
        assert resta(3,3) == 0
        assert resta(-5,3) == -8
        assert resta(-7,-4) == -3