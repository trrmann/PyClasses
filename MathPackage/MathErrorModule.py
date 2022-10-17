# MathError.py
from ClassesPackage.ClassesErrorModule import ClassesError
from MathPackage.MathModule import Math

class MathError(ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Math=Math()):
        super().__init__(str(msg), classes)
 
    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"