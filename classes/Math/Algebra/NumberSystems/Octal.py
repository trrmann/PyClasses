# Octal.py
from Classes.Math.Algebra.NumberSystems.NumberSystem import NumberSystem, NumberSystemError

class OctalError(NumberSystemError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Octal(NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Octal"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
