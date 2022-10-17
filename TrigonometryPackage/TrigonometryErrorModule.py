# TrigonometryError.py
from GeometryPackage.GeometryErrorModule import GeometryError
from TrigonometryPackage.TrigonometryModule import Trigonometry

class TrigonometryError(GeometryError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Trigonometry=Trigonometry()):
        super().__init__(str(msg))
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"