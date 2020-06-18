#coding:utf-8
import os
import yaml
def readyaml(yamlname):
    u'''读取yaml文件'''
    curpath=os.path.realpath(__file__) #当前文件路径
    dirpath=os.path.dirname(curpath) #上一层目录
    filepath=os.path.join(dirpath,yamlname) #获取yaml路径
    f=open(filepath,'r',encoding='utf-8') 
    yamldata=f.read()
    d=yaml.load(yamldata)  #将yaml 转字典
    return d
