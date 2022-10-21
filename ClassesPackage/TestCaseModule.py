# testCaseModule.py
from ClassesPackage.ClassesModule import Classes
import sys
import os
import hashlib

class TestCase(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    result_output_key = "output"
    result_std_output_key = "std_output"
    result_exception_key = "exception"

    inFileName = "test_input.txt"
    outFileName = "test_output.txt"

    # add value in
    # add instance of
    # add instance in
    # add instance of all
    # add type of
    # add type in
    # add md5 chksum of
    # add md5 chksum in

    def __init__(self,
            testCaseID: str,
            testCaseName: str,
            functionName: str,
            stdInInput: str = None,
            assertCase: bool = False,
            assertFailMessage: str = None,
            expectedOutputValueOf = None,
            expectedStdOutputValueOf: str = None,
            expectedException: Exception = None,
            className: str="TestCase",
            **functionArguments
        ):
        super().__init__(className)
        self.inFileName = TestCase.inFileName
        self.outFileName = TestCase.outFileName
        self.orig_stdin = sys.stdin
        self.orig_stdout = sys.stdout
        self.testCaseID = testCaseID
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
        self.stdInInput = stdInInput
        self.assertCase = bool(assertCase)
        self.assertFailMessage = str(assertFailMessage)
        self.expectedOutputValueOf = expectedOutputValueOf
        self.expectedStdOutputValueOf = expectedStdOutputValueOf
        self.expectedException = expectedException

    def to_string(self):
        out = f"("
        out = f"{out}className=\"{self.className}\""
        out = f"{out}, testCaseID=\"{self.testCaseID}\""
        out = f"{out}, testCaseName=\"{self.testCaseName}\""
        out = f"{out}, functionName=\"{self.functionName}\""
        out = f"{out}, functionArguments=\"{self.functionArguments}\""
        out = f"{out}, functionKeyWordArguments=\"{self.functionKeyWordArguments}\""
        out = f"{out}, expectedOutputValueOf=\"{self.expectedOutputValueOf}\""
        out = f"{out}, expectedStdOutputValueOf=\"{self.expectedStdOutputValueOf}\""
        out = f"{out}, expectedException=\"{self.expectedException}\""
        if self.stdInInput != None: out = f"{out}, stdInInput=\"{self.stdInInput}\""
        out = f"{out})"
        return out

    def __repr__(self) -> str:
        return f"{type(self).__name__}{self.to_string()}"

    def md5(string: str=""):
        return {"size": len(str(string)), "hash": hashlib.md5(str(string)).hexdigest()}

    def md5sEqual(MD5One: str = None, MD5Two: str = None, **kwargs):
        sizeOne = None
        hashOne = None
        if MD5One != None:
            MD5One = TestCase.md5(str(MD5One))
        if (MD5One == None) and ("MD5One" in kwargs.keys()):
            MD5One = kwargs["MD5One"]
        if (MD5One == None) and ("StringOne" in kwargs.keys()):
            MD5One = TestCase.md5(str(kwargs["StringOne"]))
        if ("size" in MD5One.keys()) and ("hash" in MD5One.keys()):
            sizeOne = MD5One["size"]
            hashOne = MD5One["hash"]
        sizeTwo = None
        hashTwo = None
        if MD5Two != None:
            MD5Two = TestCase.md5(str(MD5Two))
        if (MD5Two == None) and ("MD5Two" in kwargs.keys()):
            MD5Two = kwargs["MD5Two"]
        if (MD5Two == None) and ("StringTwo" in kwargs.keys()):
            MD5Two = TestCase.md5(str(kwargs["StringTwo"]))
        if ("size" in MD5Two.keys()) and ("hash" in MD5Two.keys()):
            sizeTwo = MD5Two["size"]
            hashTwo = MD5Two["hash"]
        if (sizeOne != None) and (hashOne != None) and (sizeTwo != None) and (hashTwo != None):
            return (sizeOne == sizeTwo) and (hashOne == hashTwo)
        else: return False

    # add md5 in md5s

    def stringsEqual(stringOne: str = None, stringTwo: str = None, md5TestLowestSizeLimit: int=256):
        if (stringOne == None) or (stringTwo == None):  return (stringOne == None) and (stringTwo == None)
        if int(md5TestLowestSizeLimit) < 64: md5TestLowestSizeLimit = 64
        if len(str(stringOne)) == len(str(stringTwo)):
            if len(str(stringOne)) >= int(md5TestLowestSizeLimit): return TestCase.md5sEqual(str(stringOne), str(stringTwo))
            else: return str(stringOne) == str(stringTwo)
        else: return False

    # add string in strings

    def execute(self, **kwargs):
        functionDictionary = kwargs["functionDictionary"]
        resultsDictionary = {}
        TestCase.setup_method(self = self)
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
        resultsDictionary[self.result_std_output_key] = TestCase.get_output(self = self)
        TestCase.cleanup(self = self)
        return resultsDictionary

    def eval_results(self, **kwargs):
        resultsDictionary = kwargs["resultsDictionary"]
        result = True
        if self.expectedOutputValueOf != None:
            if self.assertCase and self.assertFailMessage != None:
                assert TestCase.stringsEqual(resultsDictionary[self.result_output_key], self.expectedOutputValueOf), self.assertFailMessage
            elif self.assertCase:
                assert(TestCase.stringsEqual(resultsDictionary[self.result_output_key], self.expectedOutputValueOf))
            else:
                result = result and TestCase.stringsEqual(resultsDictionary[self.result_output_key], self.expectedOutputValueOf)
        elif self.result_output_key in resultsDictionary:
            if self.assertCase and self.assertFailMessage != None:
                assert (resultsDictionary[self.result_output_key] == None), self.assertFailMessage
            elif self.assertCase:
                assert((resultsDictionary[self.result_output_key] == None))
            else:
                result = result and (resultsDictionary[self.result_output_key] == None)
        if self.expectedStdOutputValueOf != None:
            if self.assertCase and self.assertFailMessage != None:
                assert TestCase.stringsEqual(resultsDictionary[self.result_std_output_key], self.expectedStdOutputValueOf), self.assertFailMessage
            elif self.assertCase:
                assert(TestCase.stringsEqual(resultsDictionary[self.result_std_output_key], self.expectedStdOutputValueOf))
            else:
                result = result and TestCase.stringsEqual(resultsDictionary[self.result_std_output_key], self.expectedStdOutputValueOf)
        elif self.result_std_output_key in resultsDictionary:
            if self.assertCase and self.assertFailMessage != None:
                assert (resultsDictionary[self.result_std_output_key] == None), self.assertFailMessage
            elif self.assertCase:
                assert((resultsDictionary[self.result_std_output_key] == None))
            else:
                result = result and (resultsDictionary[self.result_std_output_key] == None)
        if self.expectedException != None:
            if self.assertCase and self.assertFailMessage != None:
                assert ((type(resultsDictionary[self.result_exception_key]) == self.expectedException) or (type(resultsDictionary[self.result_exception_key]) == type(self.expectedException))), self.assertFailMessage
            elif self.assertCase:
                assert(((type(resultsDictionary[self.result_exception_key]) == self.expectedException) or (type(resultsDictionary[self.result_exception_key]) == type(self.expectedException))))
            else:
                result = result and ((type(resultsDictionary[self.result_exception_key]) == self.expectedException) or (type(resultsDictionary[self.result_exception_key]) == type(self.expectedException)))
        elif self.result_exception_key in resultsDictionary:
            if self.assertCase and self.assertFailMessage != None:
                assert (resultsDictionary[self.result_exception_key] == None), self.assertFailMessage
            elif self.assertCase:
                assert((resultsDictionary[self.result_exception_key] == None))
            else:
                result = result and (resultsDictionary[self.result_exception_key] == None)
        return result

    def setup_method(self):
        if self.stdInInput != None:
            test_in_file = open(self.inFileName, "w")
            test_in_file.write(self.stdInInput)
            test_in_file.close()
            self.orig_stdin = sys.stdin
            sys.stdin = open(self.inFileName)
        if self.expectedStdOutputValueOf != None:
            if os.path.exists(self.outFileName):
                os.remove(self.outFileName)
            self.orig_stdout = sys.stdout
            sys.stdout = open(self.outFileName, "w")

    def get_input(self):
        if self.stdInInput != None:
            test_in_file = open(self.inFileName)
            input = test_in_file.read()
            test_in_file.close()
            return input
        return None

    def get_output(self):
        if self.expectedStdOutputValueOf != None:
            test_out_file = open(self.outFileName)
            output = test_out_file.read()
            test_out_file.close()
            return output
        return None

    def teardown_method(self):
        if self.stdInInput != None:
            sys.stdin = self.orig_stdin
        if self.expectedStdOutputValueOf != None:
            sys.stdout.close()
            sys.stdout = self.orig_stdout

    def cleanup(self):
        if os.path.exists(self.inFileName):
            os.remove(self.inFileName)
        if os.path.exists(self.outFileName):
            os.remove(self.outFileName)

def testCaseListToTestCaseDictionary(testCaseList = None):
    if (len(testCaseList) >= 1):
        testCaseDictionary = {}
        counter = 0
        while counter < len(testCaseList):
            testCaseDictionary[testCaseList[counter].testCaseID] = testCaseList[counter]
            counter = counter + 1
        return testCaseDictionary
    else: return {}

def testCaseDictionaryToTestCaseList(**testCaseDictionary):
    if "testCaseDictionary" in testCaseDictionary.keys():
        testCaseList = []
        testCaseDictionary["testCaseDictionary"]
        for key in testCaseDictionary["testCaseDictionary"].keys():
            testCaseList.append(testCaseDictionary["testCaseDictionary"][key])
        return testCaseList
    return []
