# testModule.py
from ClassesPackage.ClassesModule import Classes

class Test(Classes):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, functionDictionary, className: str="Test", *args, **kwargs):
        super().__init__(kwargs["className"])
        self.result_eval_results_key = "eval_results"
        self.result_test_result_key = "test_result"
        self.functionDictionary = functionDictionary
        self.testCases = kwargs["testCases"]

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, numberOfFunctionsInDictionary={len(self.functionDictionary)}, numberOfTestCases={len(self.testCases)})"

    def execute(self):
        full_results = {}
        full_results[self.result_test_result_key] = False
        for key, case in self.testCases:
            full_results[key] = case.execute(self.functionDictionary)
            full_results[key][self.result_eval_results_key] = case.eval_results(full_results[key])
            full_results[self.result_test_result_key] = full_results[self.result_test_result_key] and not full_results[key][self.result_eval_results_key]
        full_results[self.result_test_result_key] = not full_results[self.result_test_result_key]
        return full_results
