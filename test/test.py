import requests
import json
import yaml

class TestDemo:
    def test_url(self):
        data = json.dumps({"pageCount": 20, "pageNumber": 1, "pageIs": True})
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        r = requests.post("http://pangu-dev.healthdt.cn/ht-pangu-manager/web/project/page", data=data, headers=headers)
        assert r.json()["code"] == 2000