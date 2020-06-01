from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.feed_page import FeedPage
from utilities import constants
from selenium.webdriver.common.keys import Keys
from objects.login_page import LoginPage



class BlogTests(BaseTest):

    def setUp(self):
        super().setUp()
        self.feed_page = FeedPage(self.driver)
        self.login_page = LoginPage(self.driver)


    def test_feed_navigation_page(self):
        log_message(
            "test load feed page"
        )

        self.login_page.navigate_to_page()
        self.feed_page.main_navigation_feed.click()
        self.assertTrue(self.feed_page.meta_feed_page_title)
