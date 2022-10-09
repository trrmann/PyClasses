# Science.py
from Classes.Classes import Classes, ClassesError

class ScienceError(ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass

    def __repr__(self) -> str:
        return f"{type(self).__name__}"

class Science(Classes("Science")):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name})"
