# test_testCases.py
from ClassesPackage.ClassesModule import Classes

from ClassesPackage.TestModule import Test
from ClassesPackage.TestCaseModule import TestCase
from ClassesPackage.TestCaseModule import *

print(Test( "unit/functional/regression test", {
        "Classes": Classes,
        "TestCase": TestCase,
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
            "init minimum TestCase object",
            "TestCase",
            expectedOutputValueOf=TestCase(),
            functionArguments = {
                "arguments" : ("", "", "")
            }
        ),
        TestCase(
            "case 3",
            "print test string",
            "print",
            expectedStdOutputValueOf = "['Test'] {'none': None}\n",
            functionArguments = {
                "arguments" : ["Test"],
                "keyWordArguments" : {"none": None}
            }
        ),
        TestCase(
            "case 4",
            "print test string",
            "print",
            expectedStdOutputValueOf = "Test\n",
            functionArguments = {
                "arguments" : "Test"
            }
        ),
        TestCase(
            "case 5",
            "convert valid string to float",
            "float",
            expectedOutputValueOf=1.5,
            functionArguments = {
                "arguments" : "1.5",
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 6",
            "verify float is float",
            "float",
            expectedOutputValueOf=1.5,
            functionArguments = {
                "arguments" : 1.5,
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 7",
            "raise error on float conversion when invalid string passed",
            "float",
            expectedException=ValueError,
            functionArguments = {
                "arguments" : "failMe",
                "keyWordArguments" : None
            }
        ),
        TestCase(
            "case 8",
            "test input for display of correct output and correct user input passed is returned",
            "input",
            stdInInput = "5\n",
            expectedOutputValueOf = "5",
            expectedStdOutputValueOf = "Enter a value:  ",
            functionArguments = {
                "arguments" : "Enter a value:  ",
                "keyWordArguments" : None
            }
        )
    ])).execute())
