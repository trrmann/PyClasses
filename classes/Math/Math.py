# Math.py
from Classes.Classes import Classes, ClassesError

class MathError(ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Math(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Math"):
        super().__init__(self, className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
