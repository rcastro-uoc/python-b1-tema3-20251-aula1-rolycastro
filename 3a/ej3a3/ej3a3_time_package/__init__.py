# write import for convert_date_format
# write import for date_operations
try:
    from . import convert_date_format
    from . import date_operations

except ImportError as error:
    # Gestión de error: si falta algún módulo o hay un problema de importación,
    # relanzamos el error con un mensaje más claro.
    raise ImportError(
        "Error importing ej3a3_time_package modules. "
        "Check that convert_date_format.py and date_operations.py exist inside the package."
    ) from error
# Para controlar que se importa cuando se hace: from ej3a3_time_package import *
__all__ = ["convert_date_format", "date_operations"]