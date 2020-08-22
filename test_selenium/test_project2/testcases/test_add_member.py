from test_selenium.test_project2.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        #        1. 跳转到通讯录  2. 跳转到添加成员   3. 添加成员
        result = self.main.go_to_add_member().add_member("维恩").get_member()
        assert "维恩" in result



    def teardown(self):
        self.main.quit()

