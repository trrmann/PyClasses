# AlgebraError.py
from AlgebraPackage.AlgebraModule import Algebra
from ArithmaticPackage.ArithmaticErrorModule import ArithmaticError

class AlgebraError(ArithmaticError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Algebra=Algebra()):
        super().__init__(str(msg), classes)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"