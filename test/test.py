import requests
import json
import yaml

class TestDemo:
    def test_url(self):
        base_url = yaml.load(open("data.yaml"))["pangu_dev"]
        data = json.dumps({"pageCount": 20, "pageNumber": 1, "pageIs": True})
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        r = requests.post(base_url+"/ht-pangu-manager/web/project/page", data=data, headers=headers)
        assert r.json()["code"] == 2000