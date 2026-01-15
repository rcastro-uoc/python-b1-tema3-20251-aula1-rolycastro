# archivo ej3a1_operations.py

def _validate_number(value, name: str) -> None:
    # Valida que la variable de entrada sea numerico (int / float) y no booleano
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f" '{name}' debe ser un valor numerico (int - float)")
     

def add(num_1: float, num_2: float) -> float:
    # Write here your code
    _validate_number(num_1, "num_1")
    _validate_number(num_2, "num_2")    
    return num_1 + num_2
    pass


def subtract(num_1: float, num_2: float) -> float:
    # Write here your code
    _validate_number(num_1, "num_1")
    _validate_number(num_2, "num_2")    
    return num_1 - num_2
    pass


def multiply(num_1: float, num_2: float) -> float:
    # Write here your code
    _validate_number(num_1, "num_1")
    _validate_number(num_2, "num_2")    
    return num_1 * num_2
    pass


def divide(num_1: float, num_2: float) -> float:
    # Write here your code
    _validate_number(num_1, "num_1")
    _validate_number(num_2, "num_2")  

    if num_2 == 0:
        raise ZeroDivisionError("no se puede dividir por cero")

    return num_1 / num_2
    pass
