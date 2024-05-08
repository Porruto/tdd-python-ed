# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_suma(self):
        assert suma(4,5) == 9
        assert suma(-1,-2) == -3
        assert suma(-7,5) == -2
        assert suma(-7,9) == 2

    def test_resta(self):
        assert resta(10,5) == 5
        assert resta(3,3) == 0
        assert resta(-5,3) == -2
        assert resta(-7,-4) == -11

    def test_div(self):
        assert div(5,5) == 1
        assert div(2,4) == 0.5
        assert div(8,4) == 2
        assert div(10,1) == 10

    def test_multi(self):
        assert multi(3,4) == 12
        assert multi(10,2) == 20
        assert multi(-4, 5) == -20
        assert multi(-2,-6) == 12