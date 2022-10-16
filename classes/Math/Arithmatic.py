# Arithmatic.py
import Classes.Math.Math as Math

class Arithmatic(Math.Math):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Arithmatic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
