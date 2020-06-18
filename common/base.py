# coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseApp():

    def __init__(self, driver:webdriver.Remote):
        self.driver = driver
        self.size = self.driver.get_window_size()  #获取屏幕分辨率
        print('屏幕的分辨率: %s'% self.size)
#         print('屏幕的高度: %s '% self.size['height'])
#         print('屏幕的宽度: %s '% self.size['width'])
        # self.driver.find_element_by_accessibility_id()
        # self.driver.find_element_by_android_uiautomator()
        # self.driver.find_element()
        # self.driver.find_elements()

    def find(self, locator):
        u'''查找单个元素'''
        u'''loctor传字典  →→→ {'name':'登录','by':'id','value':'vvvv','timeout':'30'}'''
        u'''name的value值:要定位元素的文本信息;by的value值:定位方法(xpath,text之类的);value的value值:定位元素的路径之类的;timeout的value值:超时时间'''
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 30
        if "name" in locator:
            print("正在定位元素名称\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['by'], locator['value']))

        if locator["by"] == "desc":
            value = locator["value"]
            element =  WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_accessibility_id(value))
        elif locator["by"] == "android":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_android_uiautomator(value))
        elif locator["by"] == "text":
            value = "//*[@text='%s']" % locator["value"]
            _loc = ("xpath", value)
            element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(_loc))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(loc))
        return element

    def finds(self,locator):
        u'''查找多个元素'''
        u'''loctor传字典  →→→ {'name':'登录','by':'id','value':'vvvv','timeout':'30'}'''
        u'''name的value值:要定位元素的文本信息;by的value值:定位方法(xpath,text之类的);value的value值:定位元素的路径之类的;timeout的value值:超时时间'''
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 30
        if "name" in locator:
            print("正在定位元素名称\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['by'], locator['value']))

        if locator["by"] == "desc":
            value = locator["value"]
            elements =  WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_accessibility_id(value))
        elif locator["by"] == "android":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_android_uiautomator(value))
        elif locator["by"] == "class":
            value = locator["value"]
            elements=WebDriverWait(self.driver,timeout,0.5).until(lambda x:x.find_elements_by_class_name(value))
        elif locator["by"] == "text":
            value = "//*[@text='%s']" % locator["value"]
            _loc = ("xpath", value)
            elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(_loc))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(loc))
        return elements

    def click(self, locator):
        u'''单个元素点击操作'''
        ele = self.find(locator)
        ele.click()
    
    def clicks(self,locator,n):
        u'''点击复数中的一个,也就是list操作'''
        self.finds(locator)[n].click()
    

    def send_text(self, locator, text):
        u'''输入文本'''
        el = self.find(locator)
        el.send_keys(text)

    def clear(self, locator):
        u'''清除文本信息'''
        el = self.find(locator)
        el.clear()
        
    def back(self):
        u'''点击返回键'''
        self.driver.back()

    def swipe_up(self,duration=500,n=1):
        u'''duration代表滑动持续时间,默认0.5s; n代表滑动次数,默认1次'''
        x1=self.size['width'] * 0.5
        y1=self.size['height'] * 0.75
        y2=self.size['height'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, duration)
        print('向上滑动成功')
    def swipe_down(self,duration=500,n=1):
        u'''duration代表滑动持续时间,默认0.5s; n代表滑动次数,默认1次'''
        x1=self.size['width'] * 0.5
        y1=self.size['height'] * 0.25
        y2=self.size['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, duration)
        print('向下滑动成功')
    def swipe_right(self,duration=500,n=1):
        u'''duration代表滑动持续时间,默认0.5s; n代表滑动次数,默认1次'''
        x1=self.size['width'] * 0.75
        x2=self.size['width'] * 0.25
        y1=self.size['height'] * 0.5
        time.sleep(5)
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, duration)
        print('向右滑动成功')
    def swipe_left(self,duration=500,n=1):
        u'''duration代表滑动持续时间,默认0.5s; n代表滑动次数,默认1次'''
        x1=self.size['width'] * 0.25
        x2=self.size['width'] * 0.75
        y1=self.size['height'] * 0.5
        time.sleep(5)
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, duration)
        print('向左滑动成功')

    def is_toast_in(self, text):
        u'''定位toast'''
        toast = ('xpath', '//*[contains(@text, "%s")]' % text)
        try:
            el = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located(toast))
            print(el.text)
            if text in el.text:
                return True
            else:
                return False
        except:
            return False

    def is_element_exist(self, locator):
        u'''判断元素存在'''
        els = self.finds(locator)   # 复数定位不会报错，定位不到元素返回[]
        if len(els) < 1:
            return False
        else:
            return True

    def is_text_page(self, text):
        '''判断text在当前页面'''
        loc1 = {"by": "text", "value":text}
        return self.is_element_exist(loc1)
    
    def wait_activity(self,cur_activity,timeout):
        u'''加载activity'''
        self.driver.wait_activity(cur_activity,timeout)
    
    def start_activity(self,appPackage,startActivity):
        u'''跳转到指定的activity'''
        self.driver.start_activity(appPackage,startActivity)
    
    def get_attribute_desc(self,locator):
        u'''获取content-desc属性'''
        text=self.find(locator).get_attribute("name")
        return text
    
    def get_text(self,locator):
        u'''获取text属性'''
        text=self.find(locator).text
        return text
    
    def tap(self,x,y,z):
        u'''触摸事件'''
        self.driver.tap([(x,y)],z)
        
    
if __name__=='__main__':
    desired_caps = {"platformName": "Android",
                "deviceName": "9a762346",
                "platformVersion": "6.0.1",
                "noReset": True,
                "appPackage": "com.baidu.yuedu",
                "appActivity": "com.baidu.yuedu.splash.SplashActivity"}
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(10)
    base=BaseApp(driver)
    driver.find_element_by_accessibility_id('VIP').click()
    time.sleep(5)
    loc={'by':'desc','value':'开通'}
    base.clicks(loc,2)
        
        
    
