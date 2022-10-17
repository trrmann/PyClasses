# InvalidParameterErrorModule.py
from ClassesPackage.ClassesModule import Classes
from ClassesPackage.ClassesErrorModule import ClassesError

class InvalidParameterError(ClassesError):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, msg:  str, classObject:  Classes=Classes(), functionName:  str="Undefined", parameterName:  str="Undefined"):
        super.__init__(classObject, msg)
        self.functionName = functionName
        self.parameterName = parameterName

    def __repr__(self) -> str:
        return f"{type(self).__name__} (classes:({self.classes}), function:({self.functionName}), parameter:({self.parameterName}), msg=\"{self.msg}\")"