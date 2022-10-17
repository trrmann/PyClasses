# ClassesErrorModule.py
from ClassesPackage.ClassesModule import Classes
from ClassesPackage.ErrorModule import Error

class ClassesError(Error):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Classes=Classes()):
        super().__init__(str(msg))
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
