# test_testCases.py
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase
from ClassesPackage.TestCaseModule import *

print(Test( "unit/functional/regression test", {
        "Classes": Classes,
        "print": print,
        "float": float,
        "input": input
    }, testCases=testCaseListToTestCaseDictionary([
        TestCase(
            "case 1",
            "init empty Classes object",
            "Classes",
            expectedOutputValueOf=Classes()
        ),
        TestCase(
            "case 2",
            "print test string",
            "print",
            expected_std_output = "['Test'] {'none': None}\n",
            functionArguments = {
                "arguments" : ["Test"],
                "keyWordArguments" : {"none": None}
            }
        ),
        TestCase(
            "case 3",
            "convert valid string to float",
            "float",
            expectedOutputValueOf=1.5,
            functionArguments = {
                "arguments" : "1.5",
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 4",
            "verify float is float",
            "float",
            expectedOutputValueOf=1.5,
            functionArguments = {
                "arguments" : 1.5,
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 5",
            "raise error on float conversion when invalid string passed",
            "float",
            expected_exception=ValueError,
            functionArguments = {
                "arguments" : "failMe",
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 6",
            "test import for display of correct output and correct user input passed is returned",
            "input",
            stdin_input = "5\n",
            expectedOutputValueOf = "5",
            expected_std_output = "Enter a value:  ",
            functionArguments = {
                "arguments" : "Enter a value:  ",
                "keyWordArguments" : None
            }
        )
    ])).execute())
