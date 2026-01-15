# geometry.py
import math

# validar solo numeros positivos
def _validate_positive_number(value, name: str) -> None:
    # Valida que value sea numérico (int/float), no booleano, y mayor que 0
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"'{name}' must be a numeric value (int or float).")
    if value <= 0:
        raise ValueError(f"'{name}' must be greater than 0.")
    

def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    # Write here your code
    _validate_positive_number(side_length, "side_length")
    return side_length * side_length
    pass


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    # Write here your code
    _validate_positive_number(base_length, "base_length")
    _validate_positive_number(height, "height")
    return base_length * height
    pass


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    # Write here your code
    _validate_positive_number(base_length, "base_length")
    _validate_positive_number(height, "height")
    return (base_length * height) / 2
    pass


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    # Write here your code
    _validate_positive_number(radius, "radius")
    return math.pi * (radius ** 2)
    pass
