# testModule.py
from colorama import Fore
from colorama import Style
from ClassesPackage.ClassesModule import Classes
from ClassesPackage.TestCaseModule import *

class Test(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    result_testName_key = "testName"
    result_test_result_key = "test_result"
    result_test_pass_count_key = "test_pass_count"
    result_test_fail_count_key = "test_fail_count"
    result_test_fail_test_list_key = "test_fail_test_list"
    result_test_count_key = "test_count"
    result_testCasesDefinition = "testCaseDefinitions"
    result_eval_results_key = "eval_results"
    def __init__(self, testName: str, functionDictionary, className: str="Test", *args, **kwargs):
        super().__init__(className)
        self.result_eval_results_key = Test.result_eval_results_key
        self.result_test_result_key = Test.result_test_result_key
        self.result_test_pass_count_key = Test.result_test_pass_count_key
        self.result_test_fail_count_key = Test.result_test_fail_count_key
        self.result_test_fail_test_list_key = Test.result_test_fail_test_list_key
        self.result_test_count_key = Test.result_test_count_key
        self.result_testName_key = Test.result_testName_key
        self.result_testCasesDefinition = Test.result_testCasesDefinition
        self.testName = str(testName)
        self.functionDictionary = functionDictionary
        if "testCases" in kwargs.keys(): self.testCases = kwargs["testCases"]
        else: self.testCases = {}

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, testName={self.testName}, numberOfFunctionsInDictionary={len(self.functionDictionary)}, numberOfTestCases={len(self.testCases)})"

    def execute(self):
        full_results = {}
        full_results[self.result_test_result_key] = True
        full_results[self.result_test_pass_count_key] = 0
        full_results[self.result_test_fail_count_key] = 0
        full_results[self.result_test_count_key] = 0
        full_results[self.result_test_fail_test_list_key] = []
        full_results[self.result_testName_key] = self.testName
        for key, case in self.testCases.items():
            full_results[key] = case.execute(functionDictionary = self.functionDictionary)
            full_results[key][self.result_eval_results_key] = case.eval_results(resultsDictionary = full_results[key])
            full_results[self.result_test_result_key] = full_results[self.result_test_result_key] and full_results[key][self.result_eval_results_key]
            if full_results[key][self.result_eval_results_key]:
                full_results[self.result_test_pass_count_key] = full_results[self.result_test_pass_count_key] + 1
            else:
                full_results[self.result_test_fail_count_key] = full_results[self.result_test_fail_count_key] + 1
                full_results[self.result_test_fail_test_list_key].append(key)
            full_results[self.result_test_count_key] = full_results[self.result_test_count_key] + 1
        full_results[self.result_testCasesDefinition] = testCaseDictionaryToTestCaseList(testCaseDictionary = self.testCases)
        return full_results

def resultsToString(**kwargs):
    if "fullResults" in kwargs.keys():
        fullResults = kwargs["fullResults"]           
        output = f"{Fore.BLUE}Test Name:  {Style.BRIGHT}{fullResults[Test.result_testName_key]}{Style.RESET_ALL}"
        if fullResults[Test.result_test_result_key]: output = f"{output}{Fore.BLUE}  status:  {Fore.GREEN}{fullResults[Test.result_test_result_key]}{Style.RESET_ALL}"
        else: output = f"{output}{Fore.BLUE}  status:  {Fore.RED}{fullResults[Test.result_test_result_key]}{Style.RESET_ALL}"
        output = f"{output}\n{Fore.BLUE}  pass/fail/count:  {Fore.GREEN}{Style.BRIGHT}{fullResults[Test.result_test_pass_count_key]}{Style.RESET_ALL}/{Fore.RED}{Style.BRIGHT}{fullResults[Test.result_test_fail_count_key]}{Style.RESET_ALL}/{Fore.BLUE}{Style.BRIGHT}{fullResults[Test.result_test_count_key]}{Style.RESET_ALL}"
        output = f"{output}\n{Fore.BLUE}  failed case list:  {Fore.RED}{fullResults[Test.result_test_fail_test_list_key]}{Style.RESET_ALL}"
        testCases = fullResults[Test.result_testCasesDefinition]
        for case in testCases:
            key = case.testCaseID
            output = f"{output}\n{case.to_string(whitespace=True)}"
            testResult = fullResults[key]
            if testResult[Test.result_eval_results_key]: output = f"{output}\n{Fore.BLUE}    status:  {Fore.GREEN}{Style.BRIGHT}{testResult[Test.result_eval_results_key]}{Style.RESET_ALL}"
            else: output = f"{output}\n{Fore.BLUE}    status:  {Fore.RED}{Style.BRIGHT}{testResult[Test.result_eval_results_key]}{Style.RESET_ALL}"
            if TestCase.result_output_key in testResult.keys(): output = f"{output}\n{Fore.BLUE}    output:  {Fore.LIGHTBLACK_EX}{Style.BRIGHT}{testResult[TestCase.result_output_key]}{Style.RESET_ALL}"
            if TestCase.result_std_output_key in testResult.keys(): output = f"{output}\n{Fore.BLUE}    std output:  {Fore.BLACK}{Style.BRIGHT}{testResult[TestCase.result_std_output_key]}{Style.RESET_ALL}"
            if TestCase.result_exception_key in testResult.keys(): output = f"{output}\n{Fore.BLUE}    exception:  {Fore.RED}{testResult[TestCase.result_exception_key]}{Style.RESET_ALL}"
        return output
    return None
