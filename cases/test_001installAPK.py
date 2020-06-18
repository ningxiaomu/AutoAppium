import unittest
import uuid
import os
import requests
from appium import webdriver
import time




class Test(unittest.TestCase):
    u'''APK的初始化:下载，安装'''
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        # cls.driver=webdriver.Remote('http://127.0.0.1:%s/wd/hub' % desired_caps[0], desired_caps[1])
        # cls.base=BaseApp(cls.driver)
        # cls.log=Log()

    def ConnectPhone(self):
        #接连手机
        connectfile = os.popen('adb devices')
        list = connectfile.readlines()
        if('127.0.0.1:21503\tdevice\n' in list):
            #已连接
            print("已连接，不需要在进行连接")
        else:
            #未连接
            print("未连接")
            for i in (1,11):
                os.system("adb connect 127.0.0.1:21503")
                time.sleep(2)
                connectfile1 = os.popen('adb devices')
                list1 = connectfile1.readlines()
                connectfile1.close()
                if('127.0.0.1:21503\tdevice\n' in list1):
                    print("第"+str(i)+"次连接成功")
                    break;
                else:
                    print("第"+str(i)+"次连接失败，重连中~~~~")
        connectfile.close()


    def InstallApk(self):
        u'''安装APK'''
        #判断手机上是否含有已安装的APK
        print(type("adb shell pm list package -3"))

        if("com.yesway.mobile" in str(os.system("adb shell pm list package -3"))):
            #具有未卸载的APK
            print("具有未卸载的APK")
            os.system("adb shell pm uninstall com.yesway.mobile")
        else:
            print("不具有未卸载的APK")
            apk_path='H://Appium//APK//zhijiaxing.apk'
            os.system("adb install -d -r %s" % apk_path)
            print("APK安装成功")

    def test_01(self):
        u'''下载APK'''
        self.ConnectPhone()
        #第一步，先检查对应文件夹里是否有为删除的APK
        #downloadUrl='http://103.231.68.98/McDonald/e/6590479/0/0/0/1592203393770/package_6069.1592203393770'
        downloadUrl='http://103.231.68.98/McDonald/e/6527981/0/0/0/1592363503974/package_620.1592363503974'
        apk_response = requests.get(downloadUrl)
        appLocation='H://Appium//APK//'
        filename = appLocation+'zhijiaxing.apk'
        list=[]
        for j in os.listdir("H://Appium//APK"):
            list.append(j)
        if('zhijiaxing.apk' in list):
            os.remove("H://Appium//APK//zhijiaxing.apk")
            print("含有未删除的APK,删除成功")
            for i in (1,10):
                try:
                    # 第三步：保存文件
                    with open(filename,'wb') as f:
                        f.write(apk_response.content)
                    print("第"+str(i)+"次下载APK成功")
                except:
                    print("第"+str(i)+"次下载APK失败")
                if('baiduyuedu.apk' in list):
                    break;
        else:
            print("不具有删除的APK,不需要删除")
            for i in (1,10):
                try:
                    #filename = appLocation+str(uuid.uuid4()) + '.apk'
                    # 第三步：保存文件
                    with open(filename,'wb') as f:
                        f.write(apk_response.content)
                        print("第"+str(i)+"次下载APK成功")
                except:
                    print("第"+str(i)+"次下载APK失败")
                if('zhijiaxing.apk' in list):
                    break;

        self.InstallApk()
    def tearDown(self):
        u'''回到起始业'''
        # self.base.start_activity(APKinfo[0],APKinfo[1])

    @classmethod
    def tearDownClass(cls):
        print("over")
        # cls.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
