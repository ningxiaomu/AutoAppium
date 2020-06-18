#coding:utf-8
import unittest
from appium import webdriver
import time
from common.base import BaseApp
from devicesinfo.device import get_devices
from appInfo.read_apkinfo import apkinfo
from common.logger import Log
from page.pageelement.pages import *

desired_caps=get_devices('逍遥')
APKinfo=apkinfo('zhijiaxing.yaml')

class Test(unittest.TestCase):
    u'''测试  跳过加载页  模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Remote('http://127.0.0.1:%s/wd/hub' % desired_caps[0], desired_caps[1])
        cls.base=BaseApp(cls.driver)
        cls.log=Log()

    def test_01(self):
        u'''加载页'''
        self.log.info('测试 加载页 模块')
        self.log.info('-----测试test_01开始-----')
        try:
            self.base.click(loadingPage.华为移动服务_取消)
            self.base.click(loadingPage.马上体验)
        except:
            pass
        self.driver.wait_activity('.home.NewMainActivity',timeout=20)
        print(self.driver.current_activity)
        self.base.click(homePage.首页)
        print("点击 首页 成功")
        #断言
        result = self.base.get_text(homePage.首页)
        self.assertEqual(result,"首页")
        self.log.info('-----测试test_01结束-----')
    def tearDown(self):
        u'''回到起始业'''
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()