# TestCaseErrorModule.py
from CodeTestingPackage.TestErrorModule import TestError
from CodeTestingPackage.TestCaseModule import TestCase

class TestCaseError(TestError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg: str, classes: TestCase=TestCase("undefined", "undefined", None)):
        super().__init__(str(msg))
        self.classes = classes

    def __repr__(self) -> str:
        return f"{type(self).__name__}(classes:({self.classes}), msg=\"{self.msg}\")"
