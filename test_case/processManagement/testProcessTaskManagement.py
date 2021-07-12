# -*- coding: utf-8 -*-
'''
@Time    : 2021/7/12 17:59
@Author  : Achen
@File    : testProcessTaskManagement.py
'''
import allure

from base.processManagement.baseProcessTakManagement import BaseProcessTaskManagement
from util.handle_db import HandleDB
from util.handle_init import HandleInit

@allure.story("流程任务管理")
class TestProcessTaskManagement:

    # True 代表dev环境，False代表test环境
    flag = True
    file = HandleInit().readFile(r'\test_data\processManagement\dataProjectManager.yaml')
    if flag:
        base_url = HandleInit().readFile(r'\test_data\data.yaml')["pangu_dev"]
        dataSource = HandleDB("172.20.1.114", "ht", "HTqazwsx123.", "ht_pangu")
        head = 'dev_'
    else:
        base_url = HandleInit().readFile(r'\test_data\data.yaml')["pangu_test"]
        dataSource = HandleDB("172.20.1.116", "pangu", "tKx!U2aBAlRd", "ht_pangu")
        head = 'test_'

    @allure.title("左侧项目树")
    def test_SelectProjrctList(self):
        response = BaseProcessTaskManagement().selectProjectList(self.base_url)
        assert response.json()['code'] == 2000
