from utils.db import LongTengServer
import requests
import pytest
db = LongTengServer()


@pytest.mark.smoke
@pytest.mark.parametrize("card_number",['12443','12443','#$@@','asdf 1234','oiuy'])
# @pytest.mark.skipif(db.check_card('123456'),'卡号已存在')#环境检查
def test_add_card(card_number,db):
    print("执行查询语句"+card_number)
    db.delete_card(card_number)
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {
        "dataSourceId": "bHRz",
        "methodId": "00A",
        "CardInfo": {
            "cardNumber": card_number
        }
    }
    res = requests.post(url=url,json=data).json()
    print(res)
    assert 200 == res["code"]
    assert "添加卡成功" == res["msg"]
    assert False is res["success"]
    assert db.check_card('123456') is True
    db.delete_card('123456')

def test_add_card(card_number,db):
    print("执行查询语句"+card_number)
    db.delete_card(card_number)
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {
        "dataSourceId": "bHRz",
        "methodId": "00A",
        "CardInfo": {
            "cardNumber": card_number
        }
    }
    res = requests.post(url=url,json=data).json()
    # print(res)
    if "添加卡成功" == res["msg"]:
        print("正常添加检查")
        assert 200 == res["code"]
        assert "添加卡成功" == res["msg"]
        assert False is res["success"]
        assert db.check_card('123456') is True
        db.delete_card('123456')
    elif "该卡已添加" == res["msg"]:
        print("重复添加检查")
        assert 5000 == res["code"]
        assert "该卡已添加" == res["msg"]
        assert False == res["success"]
    elif "业务ID不能为空" == res["msg"]:
        print("参数为空检查")
        assert 301 == res["code"]
        assert "业务ID不能为空" == res["msg"]
        assert False == res["success"]
    elif "第三方平台ID不能为空!" == res["msg"]:
        print("dataSourceId为空")
        # assert