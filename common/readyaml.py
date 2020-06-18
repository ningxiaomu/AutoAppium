#coding:utf-8
import os
import yaml
def Readyaml():
    u'''读取yaml文件'''
    curpath=os.path.realpath(__file__) #当前文件路径
    dirpath=os.path.dirname(curpath) #上一层目录
    fpath=os.path.dirname(dirpath)
    filepath1=os.path.join(fpath,'config') #获取yaml路径
    filepath=os.path.join(filepath1,'eamil.yaml') #获取yaml路径
    print('邮箱配置路径为:',filepath)
    f=open(filepath,'r',encoding='utf-8') 
    yamldata=f.read()
    d=yaml.load(yamldata)  #将yaml 转字典
    return d
       
