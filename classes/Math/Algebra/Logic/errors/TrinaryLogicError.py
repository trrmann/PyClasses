# TrinaryLogicError.py
import Classes.Math.Algebra.Logic.errors.LogicError as LogicError

class TrinaryLogicError(LogicError.LogicError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"
