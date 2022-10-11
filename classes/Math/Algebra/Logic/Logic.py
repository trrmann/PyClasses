# Logic.py
from Classes.Math.Algebra.Algebra import Algebra, AlgebraError

class LogicError(AlgebraError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Logic(Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            className = "Logic"
        ):
        super().__init__(self, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
