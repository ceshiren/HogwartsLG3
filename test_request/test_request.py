import requests

corpid = "wwe653983e4c732493"
corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]


def test_get():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=labixiaoxin"
    print(requests.get(url).json())


def test_add():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data = {
        "userid": "labixiaoxin",
        "name": "蜡笔小新",
        "mobile": "10111111115",
        "department": [1]
    }
    print(requests.post(url, json=data).json())


def test_delete():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=labixiaoxin"
    print(requests.get(url).json())


def test_update():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
        "userid": "labixiaoxin",
        "name": "wangwu"
    }
    print(requests.post(url, json=data).json())
