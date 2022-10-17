# BinaryLogic.py
from LogicPackage.LogicModule import Logic

class BinaryLogic(Logic):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "BinaryLogic"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
