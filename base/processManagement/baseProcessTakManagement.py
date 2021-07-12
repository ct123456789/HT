# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/9 17:39
@Author  : Achen
@File    : baseProcessTakManagement.py
'''
import allure
import requests
from requests import RequestException


class BaseProcessTaskManagement:

    @allure.step("请求左侧项目树list接口")
    def selectProjectList(self, domain):
        '''
        流程任务管理页面-左侧的项目树
        :param domain: 域名
        :return:
        '''
        url_path = '/ht-pangu-manager/web/biz/project/list'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            response = requests.post(domain + url_path, headers=headers)
            return response
        except RequestException as e:
            print(e)