# NumberSystem.py
import Classes.Math.Algebra.Algebra as Algebra

class NumberSystem(Algebra.Algebra):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,
            className = "NumberSystem"
        ):
        super().__init__(self, className = className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
