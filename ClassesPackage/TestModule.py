# testModule.py
from ClassesPackage.ClassesModule import Classes
from ClassesPackage.TestCaseModule import *

class Test(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, testName: str, functionDictionary, className: str="Test", *args, **kwargs):
        super().__init__(className)
        self.result_eval_results_key = "eval_results"
        self.result_test_result_key = "test_result"
        self.result_test_pass_count_key = "test_pass_count"
        self.result_test_fail_count_key = "test_fail_count"
        self.result_test_fail_test_list_key = "test_fail_test_list"
        self.result_test_count_key = "test_count"
        self.result_testName_key = "testName"
        self.result_testCasesDefinition = "testCaseDefinitions"
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
        output = f"Test Name:  {fullResults[Test.result_testName_key]}"
        output = f"{output}  status:  {fullResults[Test.result_test_result_key]}"
        output = f"{output}\n  pass/fail/count:  {fullResults[Test.result_test_pass_count_key]}/{fullResults[Test.result_test_fail_count_key]}/{fullResults[Test.result_test_count_key]}"
        output = f"{output}\n  failed case list:  {fullResults[Test.result_test_fail_test_list_key]}"
        testCases = fullResults[Test.result_testCasesDefinition]
        for case in testCases:
            key = case.testCaseID
            output = f"{output}\n{case.to_string(whitespace=True)}"
            testResult = fullResults[key]
            output = f"{output}\nstatus:  {testResult[Test.result_eval_results_key]}"
            output = f"{output}\noutput:  {testResult[TestCase.result_output_key]}"
            output = f"{output}\nstd output:  {testResult[TestCase.result_std_output_key]}"
            output = f"{output}\nexception:  {testResult[TestCase.result_exception_key]}"
