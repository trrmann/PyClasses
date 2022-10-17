# ArithmaticError.py
from MathPackage.MathErrorModule import MathError

class ArithmaticError(MathError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"
