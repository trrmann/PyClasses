# unitTestModule.py

from ClassesPackage.ClassesModule import Classes
from CodeTestingPackage.TestModule import *

class UnitTest(Test):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, testName: str, functionDictionary, className: str="Test", *args, **kwargs):
        super().__init__(testName, functionDictionary, className, *args, **kwargs)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, testName={self.testName}, numberOfFunctionsInDictionary={len(self.functionDictionary)}, numberOfTestCases={len(self.testCases)})"
