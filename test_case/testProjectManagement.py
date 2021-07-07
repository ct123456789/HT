
import requests
import json
import allure

from base.baseProjectManagement import ProjectManagement
from util.handle_db import HandleDB
from util.handle_init import HandleInit

@allure.story('项目管理')
class TestDemo:

    base_url = HandleInit(r'\test_data\data.yaml').readFile()["pangu_dev"]
    dataSource = HandleDB("172.20.1.114", "ht", "HTqazwsx123.", "ht_pangu")

    @allure.title("项目管理页面-分页查询")
    def test_ProjectPage(self):
        data = json.dumps({"pageCount": 20, "pageNumber": 1, "pageIs": True})
        response = ProjectManagement().selectProjectPage(self.base_url, data)
        assert response.json()["code"] == 2000
        sql = "select * from bs_project_biz where deleted = 0 limit 20"
        data = self.dataSource.selectMySqlData(sql)
        data1 = response.json()["data"]["list"]
        if len(data) != len(data1):
            raise ValueError("接口查询结果和数据库中查询结果不一致")
        for i in range(len(data)):
            if data[i][1] != data1[i]["name"]:
                raise ValueError("接口返回结果第"+i+"条和数据库查询不一致")

    @allure.title("项目管理页面-新增项目-项目名重复")
    def test_ProjectAdd(self):
        data = json.dumps({"name": "achen的项目", "description": "test"})
        response = ProjectManagement().addProject(self.base_url,data)
        assert response.json()['code'] == 4007