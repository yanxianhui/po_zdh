from  util.HTMLTestRunner import HTMLTestRunner
from case.first_case import FirstCase
from  util.path import REPORT_PATH
import  os
import  unittest
if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(FirstCase))
    file_path = os.path.join(REPORT_PATH + '\\first_case.html')
    with open(file_path, 'wb+') as f:
        runner = HTMLTestRunner(f, verbosity=2, title="This is first123 report",
                                               description="这个是我们第一次测试报告")
        runner.run(testsuite)
