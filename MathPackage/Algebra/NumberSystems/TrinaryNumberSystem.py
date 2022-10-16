# TrinaryNumberSystem.py
import Classes.Math.Algebra.NumberSystems.NumberSystem as NumberSystem

class TrinaryNumberSystem(NumberSystem.NumberSystem):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "TrinaryNumberSystem"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
