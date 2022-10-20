# test_testCases.py

#import ClassesPackage.ClassesModule as ClassesModule
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase

functionDictionary = {"Classes": Classes}
testCase1 = TestCase("case 1", "Classes", {}, stdin_input = "", expected_output = "", expected_std_output = "", expected_exception = Exception())
testCasesDictionary = {testCase1.testCaseName: testCase1}

test = Test(functionDictionary, testCases = testCasesDictionary)

result = test.execute()