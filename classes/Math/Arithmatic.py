# Arithmatic.py
from Classes.Math.Math import Math, MathError

class ArithmaticError(MathError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Arithmatic(Math):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Arithmatic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
