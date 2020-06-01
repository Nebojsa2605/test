from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    slug = "/en-us/user/login"
    username_locator = (By.CSS_SELECTOR, "[data-testid=login-username-field]")
    pass_locator = (By.CSS_SELECTOR, "[data-testid=login-password-field]")
    login_button_locator = (By.CSS_SELECTOR, "[data-testid=login-submit-button]")
    username_required_label = (By.CSS_SELECTOR,"[data-testid=login-username-field-label]" )
    password_required_label = (By.CSS_SELECTOR,"[data-testid=login-password-field-label]" )
    go_to_the_final_step_icon = (By.CSS_SELECTOR, "[data-testid=cart-go-to-final-step]")
    choose_credit_card_icon = (By.CSS_SELECTOR, "[data-testid='Credit Card']")
    products_drop_down_button = (By.CSS_SELECTOR, "[data-testid='main-navigation-products']")
    shop_drop_down_button = (By.CSS_SELECTOR, "a:nth-of-type(6) > div > div")
    name_locator = (By.CSS_SELECTOR, "[data-testid='main-navigation-profile-dropdown-profile']")
    shop_locator = (By.CSS_SELECTOR, "[data-testid='main-navigation-shop']")
    rack_ears_locator = (By.CSS_SELECTOR, "[data-testid='shop-product-Rack Ears (for Track Rig)']")
    plus_button_locator = (By.CSS_SELECTOR, "[data-testid='product-page-quantity-button-plus']")
    add_to_chart_button_locator = (By.CSS_SELECTOR, "[data-testid='product-page-button-add-to-cart']")
    main_navigation_chart_locator = (By.CSS_SELECTOR, "[data-testid='main-navigation-cart']")
    item_price_locator = (By.CSS_SELECTOR, "[data-testid='line-item-item-price']")
    quantity_product_number_locator = (By.CSS_SELECTOR, "[data-testid='numeric-input-value']")
    total_price_locator = (By.CSS_SELECTOR, "[data-testid='cart-info-total-price']")
    alert_locator = (By.CSS_SELECTOR, "[role='alert']")
    proceed_to_checkout_locator = (By.CSS_SELECTOR, "[data-testid='cart-proceed-to-checkout']")
    go_to_the_final_step_locator = (By.CSS_SELECTOR, "[data-testid='cart-go-to-final-step']")
    choose_credit_card_locator = (By.CSS_SELECTOR, "[data-testid='Credit Card']")
    choose_credit_card_option_locator = (By.CSS_SELECTOR, "[data-testid='credit-card-option']")
    cart_terms_and_conditions_locator = (By.CSS_SELECTOR, "[data-testid='cart-terms-and-conditions']")
    checkout_pay_now_locator = (By.CSS_SELECTOR, "[data-testid='checkout-pay-now']")
    order_summery_product_locator = (By.CSS_SELECTOR, "[data-testid='order-summary-item-product-title']")
    item_in_shopping_cart_title_locator = (By.CSS_SELECTOR, "[data-testid='line-item-product-title']")
    order_summary_item_title_locator = (By.CSS_SELECTOR, "[data-testid='order-summary-item-product-title']")
    user_loged_in_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-profile]")

    main_navigation_help_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-help]")
    main_navigation_songs_locator = (By.CSS_SELECTOR, "[data-testid=main-navigation-songs-search]")
    chose_category_locator = (By.CSS_SELECTOR, "[class=css-1fhm9d9]")
    search_songs_icon_locator = (By.CSS_SELECTOR, "[class=css-22j4bx]")

    meta_help_page_title_locator = (By.CSS_SELECTOR, "meta[name='page-name'][content='help']")



    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def user_name(self):
        return self.get_present_element(self.username_locator)

    @property
    def password(self):
        return self.get_present_element(self.pass_locator)

    @property
    def login_button(self):
        return self.get_present_element(self.login_button_locator)

    @property
    def user_loged_in(self):
        return self.get_present_element(self.user_loged_in_locator)

    @property
    def username_required(self):
        return self.get_present_element(self.username_required_label)

    @property
    def password_required(self):
        return self.get_present_element(self.password_required_label)

    @property
    def proceed_to_checkout(self):
        return self.get_present_element(self.proceed_to_checkout_locator)

    @property
    def go_to_the_final_step(self):
        return self.get_present_element(self.go_to_the_final_step_locator)

    @property
    def choose_credit_card(self):
        return self.get_visible_element(self.choose_credit_card_locator)

    @property
    def credit_card_checkbox(self):
        return self.get_present_element(self.credit_card_checkbox_field)

    @property
    def products_drop_down(self):
        return self.get_visible_element(self.products_drop_down_button)

    @property
    def shop_drop_down(self):
        return self.get_present_element(self.shop_drop_down_button)

    @property
    def avatar_image(self):
        return self.get_present_element(self.user_loged_in_locator)

    @property
    def logedin_name_locator(self):
        return self.get_present_element(self.name_locator)

    def wait_until_login_button_invisible(self):
        self.wait_until_element_invisible(self.login_button_locator)

    @property
    def dropdown_shop_locator(self):
        return self.get_present_element(self.shop_locator)

    @property
    def rack_ears(self):
        return self.get_present_element(self.rack_ears_locator)

    @property
    def plus_button(self):
        return self.get_present_element(self.plus_button_locator)

    @property
    def add_to_chart(self):
        return self.get_present_element(self.add_to_chart_button_locator)

    @property
    def main_navigation_chart(self):
        return self.get_present_element(self.main_navigation_chart_locator)

    @property
    def item_price(self):
        return self.get_present_element(self.item_price_locator)

    @property
    def quantity_product_number(self):
        return self.get_present_element(self.quantity_product_number_locator)


    @property
    def total_price(self):
        return self.get_present_element(self.total_price_locator)

    def wait_until_alert_present(self):
        self.wait_until_element_present(self.alert_locator)

    @property
    def choose_credit_card_option(self):
        return self.get_present_element(self.choose_credit_card_option_locator)

    @property
    def cart_terms_and_conditions(self):
        return self.get_present_element(self.cart_terms_and_conditions_locator)

    @property
    def checkout_pay_now(self):
        return self.get_present_element(self.checkout_pay_now_locator)

    @property
    def order_summery_product(self):
        return self.get_present_element(self.order_summery_product_locator)

    @property
    def cart_product_title(self):
        return self.get_present_element(self.cart_terms_and_conditions_locator)

    @property
    def item_in_shopping_cart(self):
        return self.get_present_element(self.item_in_shopping_cart_title_locator)

    @property
    def order_summary_item_title(self):
        return self.get_present_element(self.order_summary_item_title_locator)



    @property
    def main_navigation_help(self):
        return self.get_present_element(self.main_navigation_help_locator)

    @property
    def main_navigation_songs(self):
        return self.get_present_element(self.main_navigation_songs_locator)

    def wait_until_chose_category_present(self):
        self.wait_until_element_present(self.chose_category_locator)

    def wait_until_search_songs_icon_locator_present(self):
        self.wait_until_element_present(self.search_songs_icon_locator)



    @property
    def meta_help_page_title(self):
        return self.get_present_element(self.meta_help_page_title_locator)
