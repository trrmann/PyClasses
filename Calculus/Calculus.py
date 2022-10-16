# Calculus.py
import Classes.Math.Trigonometry.Trigonometry as Trigonometry

class Calculus(Trigonometry.Trigonometry):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Calculus"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
