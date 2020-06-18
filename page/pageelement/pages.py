# -*- coding: utf-8 -*-

from page.pageelement import tools

pages = tools.parseyaml()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class Level_1:
    书城_VIP全站去广告 = get_locater('Level_1', '书城_VIP全站去广告')
    我的 = get_locater('Level_1', '我的')
    我的_我的阅读记录 = get_locater('Level_1', '我的_我的阅读记录')
    我的_我的收藏 = get_locater('Level_1', '我的_我的收藏')
    我的_我的购买 = get_locater('Level_1', '我的_我的购买')
    我的_在线反馈 = get_locater('Level_1', '我的_在线反馈')
    圈子 = get_locater('Level_1', '圈子')
    书架 = get_locater('Level_1', '书架')
    书城_搜索 = get_locater('Level_1', '书城_搜索')

    
class Level_2:
    VIP_规则详情 = get_locater('Level_2', 'VIP_规则详情')
    VIP_开通_复数 = get_locater('Level_2', 'VIP_开通_复数')
    VIP_开通VIP会员 = get_locater('Level_2', 'VIP_开通VIP会员')
    VIP_古代言情_更多 = get_locater('Level_2', 'VIP_古代言情_更多')
    我的阅读记录_杜月笙全传 = get_locater('Level_2', '我的阅读记录_杜月笙全传')
    在线反馈_如何充值阅读币 = get_locater('Level_2', '在线反馈_如何充值阅读币')
    我的收藏_添加到购物车 = get_locater('Level_2', '我的收藏_添加到购物车')
    我的收藏_购物车 = get_locater('Level_2', '我的收藏_购物车')
    书城_搜索_输入文本 = get_locater('Level_2', '书城_搜索_输入文本')
    书城_搜索_点击搜索 = get_locater('Level_2', '书城_搜索_点击搜索')

    
class Level_3:
    VIP_规则详情_帮助中心 = get_locater('Level_3', 'VIP_规则详情_帮助中心')
    VIP_古代言情_更多 = get_locater('Level_3', 'VIP_古代言情_更多')
    VIP_开通_收银台 = get_locater('Level_3', 'VIP_开通_收银台')
    在线反馈_如何充值阅读币_解决了 = get_locater('Level_3', '在线反馈_如何充值阅读币_解决了')
    在线反馈_如何充值阅读币_如何充值阅读币 = get_locater('Level_3', '在线反馈_如何充值阅读币_如何充值阅读币')
    我的收藏_购物车_删除 = get_locater('Level_3', '我的收藏_购物车_删除')
    我的收藏_购物车_去书城逛逛 = get_locater('Level_3', '我的收藏_购物车_去书城逛逛')
    我的收藏_购物车_删除_确定 = get_locater('Level_3', '我的收藏_购物车_删除_确定')

    
class homePage:
    首页 = get_locater('homePage', '首页')

    
class loadingPage:
    华为移动服务_取消 = get_locater('loadingPage', '华为移动服务_取消')
    马上体验 = get_locater('loadingPage', '马上体验')

    