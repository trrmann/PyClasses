# Math.py
from ClassesPackage.ClassesModule import Classes

class Math(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Math"):
        super().__init__(className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"