# arithmetic.py
import math

def _validate_number(value, name: str) -> None:
	# Asegurar que value sea numerico (int - float) y no booleano
	if isinstance(value, bool) or not isinstance(value, (int, float)):
		raise ValueError(f" '{name}' debe ser un valor numerico int/float")
		

def power(base: float, exponent: float) -> float:
	# Write your code here
	_validate_number(base, "base")
	_validate_number(exponent, "exponent")
	return base ** exponent
	

def square_root(num_1: float) -> float:
	# Write your code here
	_validate_number(num_1, "num_1")

	if num_1 < 0:
		raise ValueError("No se puede calcular la raiz de un numero negativo")
	return math.sqrt(num_1)
	pass


