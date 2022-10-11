# BinaryLogic.py
from Classes.Math.Algebra.Logic.Logic import Logic, LogicError

class BinaryLogicError(LogicError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class BinaryLogic(Logic):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "BinaryLogic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
