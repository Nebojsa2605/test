from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.login_page import BlogPage
from utilities import constants
from selenium.webdriver.common.keys import Keys
import time


class LoginTests(BaseTest):

    username_correct_validation_message = "Username or E-mail is required!"
    password_correct_validation_message = "Password is required!"

    def setUp(self):
        super().setUp()
        self.login_page = BlogPage(self.driver)

    def test_login_1_4(self):
        log_message(
            "login."
        )

        self.login_page.navigate_to_page()
        self.login_page.user_name.send_keys(constants.VALID_USERNAME)
        self.login_page.password.send_keys(constants.VALID_PASSWORD)
        self.login_page.login_button.click()
        self.login_page.save_screenshot("login")
        self.login_page.avatar_image.click()
        self.assertTrue(self.login_page.logedin_name_locator.text == constants.VALID_USERNAME)
        #self.assertTrue(self.login_page.user_loged_in)




    def test_validation_message_1_5(self):
        log_message(
            "validation message test"
        )

        self.login_page.navigate_to_page()
        self.login_page.login_button.click()

        username_error_label = self.login_page.username_required
        password_error_label = self.login_page.password_required
        self.login_page.save_screenshot("validation_messages")
        self.assertTrue(username_error_label.text == self.username_correct_validation_message)
        self.assertTrue(password_error_label.text == self.password_correct_validation_message)

    def test_buy_product(self):
        log_message(
            "buy product"
        )

        self.login_page.navigate_to_page()
        self.login_page.user_name.send_keys("nesica")
        self.login_page.password.send_keys("infinum1")
        self.login_page.login_button.click()
        self.login_page.wait_until_login_button_invisible()
        self.login_page.products_drop_down.click()
        self.login_page.products_drop_down.click()
        self.login_page.dropdown_shop_locator.click()
        self.login_page.rack_ears.click()
        self.login_page.plus_button.click()
        self.login_page.add_to_chart.click()
        self.login_page.wait_until_alert_present()
        self.login_page.main_navigation_chart.click()

        single_price = float(self.login_page.item_price.text.strip("$"))

        quantity_number = float(self.login_page.quantity_product_number.text)

        total_amount = single_price * quantity_number

        cart_total_amount = float(self.login_page.total_price.text.strip("$"))

        self.assertTrue(cart_total_amount == total_amount)




    def test_buy_product17(self):
        log_message(
            "buy product"
        )

        self.login_page.navigate_to_page()
        self.login_page.user_name.send_keys("nesica")
        self.login_page.password.send_keys("infinum1")
        self.login_page.login_button.click()
        self.login_page.wait_until_login_button_invisible()
        self.login_page.products_drop_down.click()
        self.login_page.products_drop_down.click()
        self.login_page.dropdown_shop_locator.click()
        self.login_page.rack_ears.click()
        self.login_page.add_to_chart.click()
        self.login_page.wait_until_alert_present()
        self.login_page.main_navigation_chart.click()
        self.login_page.proceed_to_checkout.click()
        self.login_page.go_to_the_final_step.click()
        self.login_page.choose_credit_card.click()
        self.login_page.choose_credit_card_option.click()
        self.login_page.cart_terms_and_conditions.send_keys(Keys.SPACE)
        item_title_shoping_cart = self.login_page.item_in_shopping_cart.text
        self.login_page.checkout_pay_now.click()
        item_title_order_summery = self.login_page.order_summary_item_title.text
        self.assertTrue(item_title_order_summery == item_title_shoping_cart)

    #zad_18
    def test_load_page_test(self):
        log_message(
            "test load page"
        )

        self.login_page.navigate_to_page()
        self.login_page.user_name.send_keys(constants.VALID_USERNAME)
        self.login_page.password.send_keys(constants.VALID_PASSWORD)
        self.login_page.login_button.click()
        self.login_page.wait_until_login_button_invisible()
        self.login_page.main_navigation_feed.click()
        feed_page_title = self.driver.title
        self.assertTrue(feed_page_title == "Loop Feed | Loop Community")
        self.login_page.main_navigation_help.click()
        self.login_page.wait_until_chose_category_present()
        help_page_title = self.driver.title
        self.assertTrue(help_page_title == "Help | Loop Community")
        self.login_page.main_navigation_songs.click()
        self.login_page.wait_until_search_songs_icon_locator_present()
        songs_page_title = self.driver.title
        self.assertTrue(songs_page_title == "Songs | Loop Community")

    #18_drugi pokusaj


    def test_load_feed_page_test_meta(self):
        log_message(
            "test load feed page"
        )

        self.login_page.navigate_to_page()
        self.login_page.main_navigation_feed.click()
        self.assertTrue(self.login_page.meta_feed_page_title)

    def test_load_help_page_test_meta(self):
        log_message(
            "test help feed page"
        )

        self.login_page.navigate_to_page()
        self.login_page.main_navigation_help.click()
        self.assertTrue(self.login_page.meta_help_page_title)
