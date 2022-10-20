# test_testCases.py

#import ClassesPackage.ClassesModule as ClassesModule
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase

functionDictionary = {"Classes": Classes,
                      "print": print,
                      "float": float}
testCase1 = TestCase(testCaseName="case 1", functionName="Classes")
testCase2 = TestCase("case 2", "print", {"Test"}, expected_std_output="Test")
testCase3 = TestCase({"1.5"}, testCaseName="case 3", functionName="float", expected_output=1.5)
testCase4 = TestCase({"failMe"}, testCaseName="case 4", functionName="float", expected_exception=ValueError)
testCasesDictionary = {testCase1.testCaseName: testCase1,
                        testCase2.testCaseName: testCase2,
                        testCase3.testCaseName: testCase3,
                        testCase4.testCaseName: testCase4}

test = Test(functionDictionary, testCases = testCasesDictionary)

result = test.execute()

print(result)