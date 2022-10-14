# HexadecimalError.py
from Classes.Math.Algebra.NumberSystems.errors.NumberSystemError import NumberSystemError

class HexadecimalError(NumberSystemError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"
