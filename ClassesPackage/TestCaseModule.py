# testCaseModule.py
from ClassesPackage.ClassesModule import Classes
import sys
import os


class TestCase(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    result_input_key = "input"
    result_kw_input_key = "keyWordInput"
    result_output_key = "output"
    result_std_input_key = "std_input"
    result_std_output_key = "std_output"
    result_exception_key = "exception"

    inFileName = "test_input.txt"
    outFileName = "test_output.txt"

    def __init__(self,
            testCaseName: str,
            functionName: str,
            stdin_input: str = None,
            expected_output = None,
            expected_std_output: str = None,
            expected_exception: Exception = None,
            className: str="TestCase",
            **functionArguments
        ):
        super().__init__(className)
        self.inFileName = TestCase.inFileName
        self.outFileName = TestCase.outFileName
        self.orig_stdin = sys.stdin
        self.orig_stdout = sys.stdout
        self.testCaseName = testCaseName
        self.functionName = functionName
        if len(functionArguments) > 0:
            if "functionArguments" in functionArguments.keys():
                if(len(functionArguments["functionArguments"])) > 0:
                    if "arguments" in functionArguments["functionArguments"].keys():
                        self.functionArguments = functionArguments["functionArguments"]["arguments"]
                    else:
                        self.functionArguments = None
                    if "keyWordArguments" in functionArguments["functionArguments"].keys():
                        self.functionKeyWordArguments = functionArguments["functionArguments"]["keyWordArguments"]
                    else:
                        self.functionKeyWordArguments = None
                else:
                    self.functionArguments = None
                    self.functionKeyWordArguments = None
            else:
                self.functionArguments = None
                self.functionKeyWordArguments = None
        else:
            self.functionArguments = None
            self.functionKeyWordArguments = None
        self.stdin_input = stdin_input
        self.expected_output = expected_output
        self.expected_std_output = expected_std_output
        self.expected_exception = expected_exception

    def to_string(self):
        out = f"("
        out = f"{out}className={self.className}"
        out = f"{out}, testCaseName={self.testCaseName}"
        out = f"{out}, functionName={self.functionName}"
        out = f"{out}, functionArguments={self.functionArguments}"
        out = f"{out}, functionKeyWordArguments={self.functionKeyWordArguments}"
        if self.stdin_input != None: out = f"{out}, stdin_input={self.stdin_input}"
        out = f"{out})"
        return out

    def __repr__(self) -> str:
        return f"{type(self).__name__}{self.to_string()}"

    def execute(self, **kwargs):
        functionDictionary = kwargs["functionDictionary"]
        resultsDictionary = {}
        TestCase.setup_method(self = self)
        resultsDictionary[self.result_input_key] = self.functionArguments
        resultsDictionary[self.result_kw_input_key] = self.functionKeyWordArguments
        try:
            if (self.functionArguments == None) and (self.functionKeyWordArguments == None):
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)()
            elif (self.functionArguments == None):
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionKeyWordArguments)
            elif (self.functionKeyWordArguments == None):
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments)
            else:
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments, self.functionKeyWordArguments)
        except Exception as ex:
            resultsDictionary[self.result_exception_key] = ex
        TestCase.teardown_method(self = self)
        resultsDictionary[self.result_std_input_key] = TestCase.get_input(self = self)
        resultsDictionary[self.result_std_output_key] = TestCase.get_output(self = self)
        TestCase.cleanup(self = self)
        return resultsDictionary

    def eval_results(self, **kwargs):
        resultsDictionary = kwargs["resultsDictionary"]
        print(self)
        print(resultsDictionary)
        result = True
        print(f"exc({self.expected_exception})({type(self.expected_exception)})")
        if self.result_exception_key in resultsDictionary.keys(): print(f"exc({resultsDictionary[self.result_exception_key]})({type(resultsDictionary[self.result_exception_key])})")
        if self.expected_output != None:
            result = result and (resultsDictionary[self.result_output_key] == self.expected_output)
        if self.expected_std_output != None:
            result = result and (resultsDictionary[self.result_std_output_key] == self.expected_std_output)
        if self.expected_exception != None:
            result = result and (type(resultsDictionary[self.result_exception_key]) == type(self.expected_exception))
        return result

    def setup_method(self):
        if self.stdin_input != None:
            test_in_file = open(self.inFileName, "w")
            test_in_file.write(self.stdin_input)
            test_in_file.close()
            self.orig_stdin = sys.stdin
            sys.stdin = open(self.inFileName)
        if self.expected_std_output != None:
            if os.path.exists(self.outFileName):
                os.remove(self.outFileName)
            self.orig_stdout = sys.stdout
            sys.stdout = open(self.outFileName, "w")

    def get_input(self):
        if self.stdin_input != None:
            test_in_file = open(self.inFileName)
            input = test_in_file.read()
            test_in_file.close()
            return input
        return None

    def get_output(self):
        if self.expected_std_output != None:
            test_out_file = open(self.outFileName)
            output = test_out_file.read()
            test_out_file.close()
            return output
        return None

    def teardown_method(self):
        if self.stdin_input != None:
            sys.stdin = self.orig_stdin
        if self.expected_std_output != None:
            sys.stdout.close()
            sys.stdout = self.orig_stdout

    def cleanup(self):
        if os.path.exists(self.inFileName):
            os.remove(self.inFileName)
        if os.path.exists(self.outFileName):
            os.remove(self.outFileName)
