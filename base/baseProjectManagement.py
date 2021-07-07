# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/7 13:51
@Author  : Achen
@File    : baseProjectManagement.py
'''
import requests


class ProjectManagement:

    def selectProjectPage(self, domain, data):
        '''
        请求项目管理-分页查询接口，进入页面默认请求此接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return: 返回接口响应
        '''
        url_path = '/ht-pangu-manager/web/project/page'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        response = requests.post(domain + url_path, data=data, headers=headers)
        return response

    def addProject(self, domain, data):
        '''
        项目管理-新增项目接口
        :param domain: 域名-环境
        :param data: 请求参数
        :return:
        '''
        url_path = '/ht-pangu-manager/web/project/add'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        response = requests.post(domain + url_path, data=data, headers=headers)
        return response