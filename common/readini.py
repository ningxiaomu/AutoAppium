#coding:utf-8
import configparser
class HanddleIni():
    u'''对配置文件进行操作读，该，增'''
    def __init__(self,testfile):
        self.con=configparser.ConfigParser()
        self.con.read(testfile)
    def readini(self,section,option):
        try:
            value=self.con.get(section, option)
            #print(value)
            return value
        except Exception as msg:
            print('读取发生错误: %s' % msg)
    def modfiyini(self,file,section,key,option):
        u'''修改指定section的option值'''
        try:
            self.con.set(section,key,option)
            self.con.write(open(file,'w'))
        except Exception as msg:
            print('修改发生错误了:%s' % msg)
    def add_section(self,section,file):
        u'''新增section'''
        try:
            self.con.add_section(section)
            self.con.write(open(file,'w'))
        except Exception as msg:
            print('添加发生错了: %s' % msg)
if __name__=='__main__':
    testfile='D:\\1.ini'
    a=HanddleIni(testfile)
    a.readini('database','port')
    a.add_section(section='luobo1',file=testfile)
    a.modfiyini(file=testfile, section='database', key='port', option='123456')