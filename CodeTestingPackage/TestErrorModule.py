# TestErrorModule.py
from ClassesPackage.ClassesErrorModule import ClassesError
from CodeTestingPackage.TestModule import Test

class TestError(ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: Test=Test()):
        super().__init__(str(msg))
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
