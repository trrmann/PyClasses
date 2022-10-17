# TrinaryNumberSystem.py
from NumberSystemsPackage.NumberSystemModule import NumberSystem

class TrinaryNumberSystem(NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "TrinaryNumberSystem"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
