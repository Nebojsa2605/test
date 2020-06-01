from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class FeedPage(BasePage):

    slug = ""

    def navigate_to_page(self):
        self.navigate(self.slug)

    main_navigation_feed_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-feed]")
    meta_feed_page_title_locator = (By.CSS_SELECTOR, "meta[name='page-name'][content='feed']")

    @property
    def main_navigation_feed(self):
        return self.get_present_element(self.main_navigation_feed_locator)

    @property
    def meta_feed_page_title(self):
        return self.get_present_element(self.meta_feed_page_title_locator)