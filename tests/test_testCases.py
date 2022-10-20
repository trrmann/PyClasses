# test_testCases.py

#import ClassesPackage.ClassesModule as ClassesModule
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase

functionDictionary = {"Classes": Classes,
                      "print": print,
                      "float": float}
testCase1 = TestCase(
        testCaseName = "case 1",
        functionName = "Classes"
    )
arguments = ["Test"]
kwargs = {"none": None}
testCase2 = TestCase(
        testCaseName = "case 2",
        functionName = "print",
        expected_std_output = "Test",
        functionArguments = {
            "arguments" : arguments,
            "keyWordArguments" : kwargs
        }
    )
arguments = ["1.5"]
testCase3 = TestCase(
        testCaseName = "case 3",
        functionName = "float",
        expected_output=1.5
    )
arguments = ["failMe"]
testCase4 = TestCase(
        testCaseName = "case 4",
        functionName = "float",
        expected_exception=ValueError
    )
testCasesDictionary = {testCase1.testCaseName: testCase1,
                        testCase2.testCaseName: testCase2,
                        testCase3.testCaseName: testCase3,
                        testCase4.testCaseName: testCase4}

test = Test(functionDictionary, testCases = testCasesDictionary)

result = test.execute()

print(result)