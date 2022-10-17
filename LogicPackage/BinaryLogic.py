# BinaryLogic.py
import Classes.Math.Algebra.Logic.Logic as Logic

class BinaryLogic(Logic.Logic):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "BinaryLogic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
