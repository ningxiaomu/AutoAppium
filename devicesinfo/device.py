#coding:utf-8
u'''读取yaml 文件  desired_caps
           封装成一个函数'''
import os
import yaml

def get_devices(devicename):
    yaml.warnings({'YAMLLoadWarning': False})
    curpath=os.path.realpath(__file__) #当前文件路径
    dirpath=os.path.dirname(curpath) #上一层目录
    filepath=os.path.join(dirpath,'devices.yaml') #获取yaml路径
    print('设备配置地址:',filepath)
    f=open(filepath,'r',encoding='utf-8') 
    yamldata=f.read()
    d=yaml.load(yamldata)  #将yaml 转字典

    for i in d:
        if devicename in i['desc']:
            devicename=i['desired_caps']['deviceName']
            return (i['port'],i['desired_caps'])
if __name__=='__main__':
    print(get_devices('小米'))
    
    
    
