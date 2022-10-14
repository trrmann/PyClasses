# Octal.py
from Classes.Math.Algebra.NumberSystems.NumberSystem import NumberSystem

class Octal(NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Octal"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
