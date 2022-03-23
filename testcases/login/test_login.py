import pytest
from api.login import login
import requests
from common.readyml import read_yml_data
from config.config import root_path
import os
import allure

yml_path = os.path.join(root_path, "data", "test_login.yml")
test_data = read_yml_data(yml_path)
print("test_login_case测试数据：", test_data)




@pytest.mark.parametrize("test_input, expected", test_data)
@allure.story('这是一个用例')
def test_login_case(test_input, expected):
    '''登录用例'''
    print("测试输入：", test_input)
    s = requests.session()
    r = login(s, test_input["username"], test_input["password"])
    print(r.json())
    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]
