# Algebra.py
from ArithmaticPackage.ArithmaticModule import Arithmatic

class Algebra(Arithmatic):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Algebra"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
