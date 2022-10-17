# CalculusError.py
from CalculusPackage.CalculusModule import Calculus
from TrigonometryPackage.TrigonometryErrorModule import TrigonometryError

class CalculusError(TrigonometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Calculus=Calculus()):
        super().__init__(str(msg))
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"