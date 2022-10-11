# TrinaryLogic.py
from Classes.Math.Algebra.Logic.Logic import Logic, LogicError

class TrinaryLogicError(LogicError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class TrinaryLogic(Logic):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "TrinaryLogic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
