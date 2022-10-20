# test_testCases.py

#import ClassesPackage.ClassesModule as ClassesModule
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase

functionDictionary = {"Classes": Classes,
                      "print": print,
                      "float": float,
                      "input": input}
testCase1 = TestCase(
        "case 1",
        "Classes",
        expected_output=Classes()
    )
arguments = ["Test"]
kwargs = {"none": None}
testCase2 = TestCase(
        "case 2",
        "print",
        expected_std_output = "['Test'] {'none': None}\n",
        functionArguments = {
            "arguments" : arguments,
            "keyWordArguments" : kwargs
        }
    )
arguments = "1.5"
testCase3 = TestCase(
        "case 3",
        "float",
        expected_output=1.5,
        functionArguments = {
            "arguments" : arguments,
            "keyWordArguments" : None
        }
    )
arguments = 1.5
testCase4 = TestCase(
        "case 4",
        "float",
        expected_output=1.5,
        functionArguments = {
            "arguments" : arguments,
            "keyWordArguments" : None
        }
    )
arguments = "failMe"
testCase5 = TestCase(
        "case 5",
        "float",
        expected_exception=ValueError,
        functionArguments = {
            "arguments" : arguments,
            "keyWordArguments" : None
        }
    )

testCase6 = TestCase(
        "case 6",
        "input",
        stdin_input = "5\n",
        expected_output = "5",
        expected_std_output = "Enter a value:  ",
        functionArguments = {
            "arguments" : "Enter a value:  ",
            "keyWordArguments" : None
        }
    )

testCasesDictionary = {testCase1.testCaseName: testCase1,
                        testCase2.testCaseName: testCase2,
                        testCase3.testCaseName: testCase3,
                        testCase4.testCaseName: testCase4,
                        testCase5.testCaseName: testCase5,
                        testCase6.testCaseName: testCase6}

test = Test(functionDictionary, testCases = testCasesDictionary)

result = test.execute()

print(result)