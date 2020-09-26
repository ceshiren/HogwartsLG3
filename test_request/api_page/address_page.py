from test_request.api_page.base_api import BaseApi
from test_request.api_page.wework_utils import WeWorkUtils


class AddressPage(BaseApi):
    """
    通讯录管理，包括增删改查
    """

    def __init__(self):
        _corpsecret = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        utils = WeWorkUtils()
        self.token = utils.get_token(_corpsecret)

    def get_member_info(self):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.token, "userid": "labixiaoxin"}
        }
        return self.send_api(data)

    def add_member(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            "json": {"userid": "labixiaoxin", "name": "蜡笔小新",
                     "mobile": "10111111115", "department": [1]}}
        return self.send_api(data)

    def delete_member(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=labixiaoxin",
            "method": "get"
        }
        return self.send_api(data)

    def update_member(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json": {
                "userid": "labixiaoxin",
                "name": "wangwu"}
        }
        return self.send_api(data)
