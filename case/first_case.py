#coding=utf-8
import sys
sys.path.append('E:\\Teacher\\Imooc\\SeleniumPython')
import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
from  util import HTMLTestRunner
from  util.path import REPORT_PATH
import unittest
import os
import time

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.file_name = "E:/Teacher/Imooc/SeleniumPython/Image/test001.png"
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')
        cls.driver.maximize_window()
    def setUp(self):

        self.driver.refresh()

        self.logger.info("this is chrome")

        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        #if sys.exc_info()[0]:
        for method_name,error in self._outcome.errors:
              if error:
                  case_name = self._testMethodName
                  file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                  self.driver.save_screenshot(file_path)
        #print("这个是case的后置调键1")

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()

    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息

    def test_login_email_error(self):
        email_error = self.login.login_email_error('13145@qq.com','user111111@qq.com','11111111',self.file_name)
        #return self.assertFalse(email_error,"测试失败")
        print('结果',email_error)
        return self.assertTrue(email_error)


    # def test_login_username_error(self):
    #     username_error = self.login.login_name_error('12123@qq.com','t1','111111',self.file_name)
    #     self.assertTrue(username_error)
    #
    # def test_login_code_error(self):
    #     code_error = self.login.login_name_error('11121@qq.com','ss22212','111111',self.file_name)
    #     self.assertFalse(code_error)
    #
    # def test_login_password_error(self):
    #     password_error = self.login.login_name_error('11311@qq.com','ss23222','111111',self.file_name)
    #     self.assertFalse(password_error)
    #
    # def test_login_success(self):
    #     success = self.login.user_base('12221@qq.com','2321','111111',self.file_name)
    #     self.assertFalse(success)
    #     #self.assert

'''    
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    file_path = os.path.join(REPORT_PATH+'\\first_case.html')
    print(file_path)
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(FirstCase))
    # suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    # #suite.addTest(FirstCase('test_login_code_error'))
    # suite.addTest(FirstCase('test_login_email_error'))
    # suite.addTest(FirstCase('test_login_username_error'))
    #unittest.TextTestRunner().run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    #f = open(file_path, 'wb+')
    # with open(file_path, 'wb+') as f:
    #      runner = HTMLTestRunner.HTMLTestRunner(f,verbosity=2,title="This is first123 report",description="这个是我们第一次测试报告")
    #      runner.run(testsuite)
