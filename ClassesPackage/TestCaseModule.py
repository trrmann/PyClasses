# testCaseModule.py
from colorama import Fore
from colorama import Style
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

    def to_string(self, whitespace: bool=False):
        white1 = ""
        white2 = ""
        white3 = ""
        if whitespace:
            white1 = "\n"
            white2 = f"{white1}    "
            white3 = f"{white2}    "
        out = f"{white1}{Fore.CYAN}({Style.RESET_ALL}"
        out = f"{out}{Fore.CYAN}className=\"{self.className}\"{Style.RESET_ALL}"
        out = f"{out}{Fore.CYAN}, testCaseID=\"{Fore.BLUE}{Style.BRIGHT}{self.testCaseID}{Fore.CYAN}\"{Style.RESET_ALL}"
        out = f"{out}{Fore.CYAN}, testCaseName=\"{Fore.BLACK}{Style.BRIGHT}{self.testCaseName}{Fore.CYAN}\"{Style.RESET_ALL}"
        out = f"{out}{Fore.CYAN}{white2}, functionName=\"{Fore.BLUE}{Style.BRIGHT}{self.functionName}{Fore.CYAN}\"{Style.RESET_ALL}"
        if (self.functionArguments != None) and (type(self.functionArguments)==type(str(""))): out = f"{out}{Fore.CYAN}, functionArguments=\"{Fore.YELLOW}{Style.BRIGHT}{self.functionArguments}{Fore.CYAN}\"{Style.RESET_ALL}"
        if (self.functionArguments != None) and (type(self.functionArguments)!=type(str(""))): out = f"{out}{Fore.CYAN}, functionArguments={Fore.YELLOW}{Style.BRIGHT}{self.functionArguments}{Style.RESET_ALL}"
        if self.functionKeyWordArguments != None: out = f"{out}{Fore.CYAN}, functionKeyWordArguments={Fore.YELLOW}{Style.BRIGHT}{self.functionKeyWordArguments}{Style.RESET_ALL}"
        if self.stdInInput != None: out = f"{out}{Fore.CYAN}, stdInInput=\"{Fore.YELLOW}{Style.BRIGHT}{self.stdInInput}{Fore.CYAN}\"{Style.RESET_ALL}"
        if (self.expectedOutputValueOf != None) and (type(self.expectedOutputValueOf)==type(str(""))): out = f"{out}{Fore.CYAN}{white3}, expectedOutputValueOf=\"{Fore.GREEN}{self.expectedOutputValueOf}{Fore.CYAN}\"{Style.RESET_ALL}"
        if (self.expectedOutputValueOf != None) and (type(self.expectedOutputValueOf)!=type(str(""))): out = f"{out}{Fore.CYAN}{white3}, expectedOutputValueOf={Fore.GREEN}{self.expectedOutputValueOf}{Style.RESET_ALL}"
        if self.expectedStdOutputValueOf != None: out = f"{out}{Fore.CYAN}{white3}, expectedStdOutputValueOf=\"{Fore.GREEN}{self.expectedStdOutputValueOf}{Fore.CYAN}\"{Style.RESET_ALL}"
        if self.expectedException != None: out = f"{out}{Fore.CYAN}{white3}, expectedException={Fore.GREEN}{self.expectedException}{Style.RESET_ALL}"
        out = f"{out}){white1}"
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
        print(self.testCaseID)
        print(self.functionName)
        print(self.functionArguments)
        print(self.functionKeyWordArguments)
        inCase="none"
        TestCase.setup_method(self = self)
        try:
            if (self.functionArguments == None) and (self.functionKeyWordArguments == None):
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)()
            elif (self.functionArguments == None):
                resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionKeyWordArguments)
            elif (self.functionKeyWordArguments == None):
                match len(self.functionArguments):
                    case 0:
                        inCase=(0)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments)
                    case 1:
                        inCase=(1)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0])
                    case 2:
                        inCase=(2)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1])
                    case 3:
                        inCase=(3)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2])
                    case 4:
                        inCase=(4)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3])
                    case 5:
                        inCase=(5)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4])
                    case 6:
                        inCase=(6)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5])
                    case 7:
                        inCase=(7)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6])
                    case 8:
                        inCase=(8)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7])
                    case 9:
                        inCase=(9)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8])
                    case 10:
                        inCase=(10)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9])
                    case 11:
                        inCase=(11)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10])
                    case 12:
                        inCase=(12)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11])
                    case 13:
                        inCase=(13)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12])
                    case 14:
                        inCase=(14)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13])
                    case 15:
                        inCase=(15)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13], self.functionArguments[14])
                    case 16:
                        inCase=(16)
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13], self.functionArguments[14], self.functionArguments[15])
            else:
                match len(self.functionArguments):
                    case 0:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments, self.functionKeyWordArguments)
                    case 1:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionKeyWordArguments)
                    case 2:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionKeyWordArguments)
                    case 3:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionKeyWordArguments)
                    case 4:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionKeyWordArguments)
                    case 5:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionKeyWordArguments)
                    case 6:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionKeyWordArguments)
                    case 7:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionKeyWordArguments)
                    case 8:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionKeyWordArguments)
                    case 9:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionKeyWordArguments)
                    case 10:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionKeyWordArguments)
                    case 11:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionKeyWordArguments)
                    case 12:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionKeyWordArguments)
                    case 13:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionKeyWordArguments)
                    case 14:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13], self.functionKeyWordArguments)
                    case 15:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13], self.functionArguments[14], self.functionKeyWordArguments)
                    case 16:
                        resultsDictionary[self.result_output_key] = functionDictionary.get(self.functionName)(self.functionArguments[0], self.functionArguments[1], self.functionArguments[2], self.functionArguments[3], self.functionArguments[4], self.functionArguments[5], self.functionArguments[6], self.functionArguments[7], self.functionArguments[8], self.functionArguments[9], self.functionArguments[10], self.functionArguments[11], self.functionArguments[12], self.functionArguments[13], self.functionArguments[14], self.functionArguments[15], self.functionKeyWordArguments)
        except Exception as ex:
            resultsDictionary[self.result_exception_key] = ex
        TestCase.teardown_method(self = self)
        print(inCase)
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
                if self.result_output_key in resultsDictionary.keys(): 
                    result = result and TestCase.stringsEqual(resultsDictionary[self.result_output_key], self.expectedOutputValueOf)
                else :
                    result = result and False
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
