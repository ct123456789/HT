import json
import allure

from base.processManagement.baseProjectManagement import BaseProjectManagement
from util.handle_db import HandleDB
from util.handle_init import HandleInit

@allure.story('项目管理')
class TestProjrctManagemnt:
    # True 代表dev环境，False代表test环境
    flag = True
    file = HandleInit().readFile(r'\test_data\processManagement\dataProjectManager.yaml')
    if flag :
        base_url = HandleInit().readFile(r'\test_data\data.yaml')["pangu_dev"]
        dataSource = HandleDB("172.20.1.114", "ht", "HTqazwsx123.", "ht_pangu")
        head = 'dev_'
    else:
        base_url = HandleInit().readFile(r'\test_data\data.yaml')["pangu_test"]
        dataSource = HandleDB("172.20.1.116", "pangu", "tKx!U2aBAlRd", "ht_pangu")
        head = 'test_'

    @allure.title("项目管理页面-分页查询")
    def test_ProjectPage(self):
        data = json.dumps(self.file['page'])
        response = BaseProjectManagement().selectProjectPage(self.base_url, data)
        assert response.json()["code"] == 2000
        sql = "select * from bs_project_biz where deleted = 0 limit 20"
        db_data = self.dataSource.selectMySqlData(sql)
        res_data = response.json()["data"]["list"]
        if len(db_data) != len(res_data):
            raise ValueError("接口查询结果和数据库中查询结果不一致")
        for i in range(len(db_data)):
            if db_data[i][1] != res_data[i]["name"]:
                raise ValueError("接口返回结果第"+i+"条和数据库查询不一致")

    @allure.title("项目管理页面-新增项目-项目名重复")
    def test_ProjectAddRepetition(self):
        param = self.file['add']
        try:
            BaseProjectManagement().addProject(self.base_url, json.dumps(param))
            sql = "select * from bs_project_biz where name = '" + param['name'] + "' and deleted = 0"
            db_data = self.dataSource.selectMySqlData(sql)
            projectId = self.head + str(db_data[0][0])
            response = BaseProjectManagement().addProject(self.base_url, json.dumps(param))
            assert response.json()['code'] == 4007
        finally:
            BaseProjectManagement().deletProject(self.base_url, json.dumps({'id': projectId}))


    @allure.title("项目管理页面-新增项目-成功")
    def test_ProjectAddError(self):
        param = self.file['add']
        try:
            response = BaseProjectManagement().addProject(self.base_url, json.dumps(param))
            assert response.json()['code'] == 2000
            sql = "select * from bs_project_biz where name = '" + param['name'] + "' and deleted = 0"
            db_data = self.dataSource.selectMySqlData(sql)
            projectId = self.head + str(db_data[0][0])
        finally:
            BaseProjectManagement().deletProject(self.base_url, json.dumps({'id': projectId}))

    @allure.title("项目管理-编辑项目")
    def test_ProjectUpdate(self):
        add_param = self.file['add']
        update_data = self.file['update']
        try:
            BaseProjectManagement().addProject(self.base_url, json.dumps(add_param))
            sql = "select * from bs_project_biz where name = '" + add_param['name'] + "' and deleted = 0"
            db_data = self.dataSource.selectMySqlData(sql)
            update_data['id'] = self.head + str(db_data[0][0])
            response = BaseProjectManagement().updateProject(self.base_url, json.dumps(update_data))
            assert response.json()['code'] == 2000
        finally:
            BaseProjectManagement().deletProject(self.base_url, json.dumps({'id': update_data['id']}))

    @allure.title("项目管理-删除项目")
    def test_ProjectDeleted(self):
        add_param = self.file['add']
        try:
            BaseProjectManagement().addProject(self.base_url, json.dumps(add_param))
            sql = "select * from bs_project_biz where name = '" + add_param['name'] + "' and deleted = 0"
            db_data = self.dataSource.selectMySqlData(sql)
            ProjectId = self.head + str(db_data[0][0])
            response = BaseProjectManagement().deletProject(self.base_url, json.dumps({'id': ProjectId}))
            assert response.json()['code'] == 2000
        finally:
            pass
