# Hexadecimal.py
import Classes.Math.Algebra.NumberSystems.NumberSystem as NumberSystem

class Hexadecimal(NumberSystem.NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Hexadecimal"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
