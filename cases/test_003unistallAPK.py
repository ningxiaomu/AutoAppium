#coding:utf-8
import unittest
from appium import webdriver
import time
import os
from common.base import BaseApp
from devicesinfo.device import get_devices
from appInfo.read_apkinfo import apkinfo
from common.logger import Log


desired_caps=get_devices('逍遥')
APKinfo=apkinfo('zhijiaxing.yaml')

class Test(unittest.TestCase):
    u'''测试  跳过加载页  模块'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Remote('http://127.0.0.1:%s/wd/hub' % desired_caps[0], desired_caps[1])
        cls.base=BaseApp(cls.driver)
        cls.log=Log()

    def test_01uninstallAPK(self):
        u'''卸载 APK'''
        #判断手机上是否含有已安装的APK
        os.system("adb shell pm uninstall com.yesway.mobile")
        self.log.info("APP卸载成功")

    def tearDown(self):
        u'''回到起始业'''
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()