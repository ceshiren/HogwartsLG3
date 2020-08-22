from test_selenium.test_project.page.add_member_page import AddMember
from test_selenium.test_project.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        #       1. 跳转到添加成员 2. 添加成员
        result = self.main.go_to_add_member().add_member("13199991111").get_member_list()
        assert "皮城女警" in result

    def test_add_member_fail(self):
        self.main.go_to_add_member().add_member("1@@@@@@@")
        result = AddMember(self.main.driver).get_phone_error_message()
        assert "请填写正确的手机号码" == result


    def test_contact_add_member(self):
        #       1. 跳转到通讯录页面 2. 跳转到添加成员 3. 添加成员
        self.main.go_to_contact().go_to_add_member().add_member()

    def teardown(self):
        self.main.base_quit()