# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/7 13:51
@Author  : Achen
@File    : baseProjectManagement.py
'''
import allure
import requests
from requests import RequestException


class BaseProjectManagement:

    @allure.step("调用分页查询接口")
    def selectProjectPage(self, domain, data):
        '''
        请求项目管理-分页查询接口，进入页面默认请求此接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return: 返回接口响应
        '''
        url_path = '/ht-pangu-manager/web/project/page'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            response = requests.post(domain + url_path, data=data, headers=headers)
            return response
        except RequestException as e:
            print(e)

    @allure.step("调用新增接口")
    def addProject(self, domain, data):
        '''
        项目管理-新增项目接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return:
        '''
        url_path = '/ht-pangu-manager/web/project/add'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            response = requests.post(domain + url_path, data=data, headers=headers)
            return response
        except RequestException as e:
            print(e)

    @allure.step("调用编辑接口")
    def updateProject(self, domain, data):
        '''
        项目管理-编辑项目接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return:
        '''
        url_path = '/ht-pangu-manager/web/project/update'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            response = requests.post(domain + url_path, data=data, headers=headers)
            return response
        except RequestException as e:
            print(e)

    @allure.step("调用删除接口")
    def deletProject(self, domain, data):
        '''
        项目管理-删除项目接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return:
        '''
        url_path = '/ht-pangu-manager/web/project/remove'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        try:
            response = requests.post(domain + url_path, data=data, headers=headers)
            return response
        except RequestException as e:
            print(e)