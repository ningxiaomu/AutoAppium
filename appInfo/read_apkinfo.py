#coding:utf-8
import yaml
import os

def apkinfo(apkname):
    yaml.warnings({'YAMLLoadWarning': False})
    curpath=os.path.realpath(__file__)
    dir1=os.path.dirname(curpath)
    yamlpath=os.path.join(dir1,apkname)
    print('APK配置信息:',yamlpath)
    f=open(yamlpath,'r',encoding='utf-8')
    file=f.read()
    info=yaml.load(file)
    for i in info:
        return (i['info']['appPackage'],i['info']['startActivity'])
    
if __name__=='__main__':
    print(apkinfo('baiduyuedu.yaml'))


    
    
