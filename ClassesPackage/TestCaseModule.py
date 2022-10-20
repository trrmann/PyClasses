# testCaseModule.py
from ClassesPackage.ClassesModule import Classes
import sys
import os

class TestCase(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    result_input_key = "input"
    result_output_key = "output"
    result_std_input_key = "std_input"
    result_std_output_key = "std_output"
    result_exception_key = "exception"

    inFileName = "test_input.txt"
    outFilename = "test_output.txt"

    def __init__(self,
            testCaseName: str,
            functionName: str,
            *arguments,
            stdin_input: str,
            expected_output,
            expected_std_output: str,
            expected_exception: Exception,
            className: str="TestCase"
        ):
        super().__init__(className)
        self.orig_stdin = sys.stdin
        self.orig_stdout = sys.stdout
        self.testCaseName = testCaseName
        self.functionName = functionName
        self.arguments = arguments
        self.stdin_input = stdin_input
        self.expected_output = expected_output
        self.expected_std_output = expected_std_output
        self.expected_exception = expected_exception

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, testCaseName={self.testCaseName}, functionName={self.functionName}, arguments={self.arguments}, stdin_input={self.stdin_input})"

    def execute(self, **kwargs):
        functionDictionary = kwargs["functionDictionary"]
        resultsDictionary = {}
        TestCase.setup_method(self = self, stdin_input = self.stdin_input)
        resultsDictionary[self.result_input_key] = self.arguments
        try:
            resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.arguments)
        except Exception as ex:
            resultsDictionary[self.result_exception_key] = ex
        TestCase.teardown_method(self = self)
        resultsDictionary[self.result_std_input_key] = TestCase.get_input(self = self)
        resultsDictionary[self.result_std_output_key] = TestCase.get_output(self = self)
        TestCase.cleanup(self = self)
        return resultsDictionary

    def eval_results(self, **kwargs):
        resultsDictionary = kwargs["resultsDictionary"]
        fail = not(resultsDictionary[self.result_output_key] == self.expected_output)
        fail = fail and not(resultsDictionary[self.result_std_output_key] == self.expected_std_output)
        fail = fail and not(resultsDictionary[self.result_exception_key] == self.expected_exception)
        return not fail

    def setup_method(self, stdin_input):
        if os.path.exists(self.outFilename):
            os.remove(self.outFilename)
        test_in_file = open(self.inFileName, "w")
        test_in_file.write(stdin_input)
        test_in_file.close()
        self.orig_stdin = sys.stdin
        self.orig_stdout = sys.stdout
        sys.stdin = open(self.inFileName)
        sys.stdout = open(self.outFilename, "w")

    def get_input(self):
        test_in_file = open(self.inFilename)
        input = test_in_file.read()
        test_in_file.close()
        return input

    def get_output(self):
        test_out_file = open(self.outFilename)
        output = test_out_file.read()
        test_out_file.close()
        return output

    def teardown_method(self):
        sys.stdin = self.orig_stdin
        sys.stdout.close()
        sys.stdout = self.orig_stdout

    def cleanup(self):
        if os.path.exists(self.inFileName):
            os.remove(self.inFileName)
        if os.path.exists(self.outFilename):
            os.remove(self.outFilename)
