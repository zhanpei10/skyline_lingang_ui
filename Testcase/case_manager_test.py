# 事件管理页面测试
import unittest
from ddt import ddt, data, unpack
from Lib.common.common_function import *
from Lib.base.page_object.login_page import LonginPage
from Lib.base.page_object.case_manager import CaseManager


@ddt
class CaseManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = choose_browser()
        cls.login = LonginPage(cls.driver)
        cls.caseManager = CaseManager(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.login.login('kobeAdmin002', 'kobe8888')

    def test_look_by_case_from(self):
        self.caseManager.look_by_case_from()


if __name__ == '__main__':
    unittest.main()
