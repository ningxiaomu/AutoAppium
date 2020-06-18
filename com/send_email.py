# coding:utf-8
import unittest
import time


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from com.common.readini import HanddleIni
# from com.common import HTMLTestRunner_jpg
import HTMLTestRunner_jpg
from readini import  HanddleIni
import smtplib
import os

parentpath=os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
inipath=os.path.join(parentpath,r'config\test.ini')
inidata=HanddleIni(inipath)
#excelresult=os.path.join(Fatherpath,r'report\result.xlsx')
# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="cases", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
                                           title=u'APP自动化测试报告',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send(ABC):
    sender = inidata.readini('email', 'sender')
    to_addrs = ['luo52638487@163.com','664952305@qq.com']
    subject = inidata.readini('email', 'subject')
    smtpserver = inidata.readini('email', 'smtpserver')
    username = inidata.readini('email', 'username')
    password = inidata.readini('email', 'password')
    
    
    msg=MIMEMultipart()
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=Header(sender)
    msg.attach(MIMEText('Dear all, \n  本周APP测试报告详见附件，如有问题请与 罗波 联系。 \n  note:请用谷歌浏览器查看附件详情', 'plain', 'utf-8'))
    
    attpart=MIMEText(open(ABC,'rb').read(),'base64','utf-8')
    attpart['Content-Type']='application/octet-stream'
    attpart['Content-Disposition']='attachment;filename="result.html"'
    msg.attach(attpart)
    
      
    smtp = smtplib.SMTP()
    smtp.connect( smtpserver )
    smtp.login( username, password )
    smtp.sendmail( sender, to_addrs, msg.as_string(),msg )
    smtp.quit()
    print ('Email has send out')


if __name__ == "__main__":
    # all_case = add_case()   # 1加载用例
    # # # 生成测试报告的路径
    # run_case(all_case)        # 2执行用例
    # # # 获取最新的测试报告文件
    # report_path = os.path.join(cur_path, "report")  # 用例文件夹
    # report_file = get_report_file(report_path)  # 3获取最新的测试报告
    # send(report_file)  # 4最后一步发送报告

    #获取report
    report_path = os.path.join(parentpath, "report")  # 用例文件夹
    report_file = get_report_file(report_path)  # 3获取最新的测试报告
    send(report_file)  # 4最后一步发送报告

  
