# Decimal.py
from NumberSystemsPackage.NumberSystemModule import NumberSystem

class Decimal(NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Decimal"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
