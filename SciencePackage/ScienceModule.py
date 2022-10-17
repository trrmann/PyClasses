# Science.py
from ClassesPackage.ClassesModule import Classes

class Science(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, className = "Science"):
        super().__init__(child=self, className=className)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className})"
