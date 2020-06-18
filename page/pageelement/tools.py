# coding:utf-8
import yaml
import os
import jinja2
# 当前脚本路径
#basepath = os.path.dirname(os.path.realpath(__file__))
curpath=os.path.realpath(__file__)
basepath=os.path.dirname(curpath)
print(basepath)

def parseyaml(yamlPagesPath=basepath):
    '''
    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f,Loader=yaml.FullLoader)
                    pageElements.update(page)
    return pageElements

def get_page_list(yamlpage):
    '''把所有的页面对象，放到list 如：
    {"MyPage": ["我的-出行服务", "我的-邀请好友"],
    "DingDan": ["订单-火车票", "订单-机票"],
    }
    '''
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        # 获取loctors定位方法
        locs = names['locators']
        # 添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

def creat_pages_py(page_list):
    '''
    用jinja2把tempetpage模板生成pages.py
    :param pagelist:get_page_list返回内容
    {"MyPage": ["我的-出行服务", "我的-邀请好友"],
    "DingDan": ["订单-火车票", "订单-机票"],
    }
    :return:
    '''
    print(os.path.join(basepath, "templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars ={
                    'page_list': page_list
                    }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath, "pages.py"), "w", encoding="utf-8") as f:
        f.write(template.render(templateVars))

if __name__ == "__main__":
    a = parseyaml()
    print(a)
    pagelists = get_page_list(a)
    print(pagelists)
    creat_pages_py(pagelists)