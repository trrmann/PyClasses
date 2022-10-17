# ArithmaticError.py
from ArithmaticPackage.ArithmaticModule import Arithmatic
from MathPackage.MathErrorModule import MathError

class ArithmaticError(MathError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Arithmatic=Arithmatic()):
        super().__init__(str(msg), classes)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"