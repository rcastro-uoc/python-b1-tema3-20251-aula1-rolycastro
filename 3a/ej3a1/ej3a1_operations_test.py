import pytest
import ej3a1_operations


def test_sumar():
    result = ej3a1_operations.add(3, 4)
    assert result == 7, "The add operation does not work"

    result = ej3a1_operations.add(-3.5, 4)
    assert result == 0.5,  "The add operation does not work"


def test_restar():
    result = ej3a1_operations.subtract(10, 5)
    assert result == 5,  "The subtract operation does not work"


def test_multiplicar():
    result = ej3a1_operations.multiply(3, 4)
    assert result == 12,  "The multiply operation does not work"


def test_dividir():
    result = ej3a1_operations.divide(8, 4)
    assert result == 2,  "The divide operation does not work"


def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        ej3a1_operations.divide(8, 0),  "The zero division operation does not work"

# Para ejecutar el test
# desde cualquier ubicacion:
# python -m pytest .\python-b1-tema3-20251-aula1-rolycastro\3a\ej3a1\ej3a1_operations_test.py -q

# Desde la ubicacion del ejecicio:
# PS C:\Users\roly-\Desktop\UOC Python 2025\B1\tema_3\python-b1-tema3-20251-aula1-rolycastro\3a\ej3a1> 
# python -m pytest ej3a1_operations_test.py -q
