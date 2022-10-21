# test_testCases.py
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase
from ClassesPackage.TestCaseModule import *

print(Test({
        "Classes": Classes,
        "print": print,
        "float": float,
        "input": input
    }, testCases=testCaseListToTestCaseDictionary([
        TestCase(
            "case 1",
            "init empty Classes object",
            "Classes",
            expected_output=Classes()
        ),
        TestCase(
            "case 2",
            "case 2",
            "print",
            expected_std_output = "['Test'] {'none': None}\n",
            functionArguments = {
                "arguments" : ["Test"],
                "keyWordArguments" : {"none": None}
            }
        ),
        TestCase(
        "case 3",
        "case 3",
        "float",
        expected_output=1.5,
        functionArguments = {
            "arguments" : "1.5",
            "keyWordArguments" : None
        }
    ),
        TestCase(
        "case 4",
        "case 4",
        "float",
        expected_output=1.5,
        functionArguments = {
            "arguments" : 1.5,
            "keyWordArguments" : None
        }
    ),
        TestCase(
        "case 5",
        "case 5",
        "float",
        expected_exception=ValueError,
        functionArguments = {
            "arguments" : "failMe",
            "keyWordArguments" : None
        }
    ),
        TestCase(
        "case 6",
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
    ])).execute())
