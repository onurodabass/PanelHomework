from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.instory_page import InstoryPage


class PartnerPage(BasePage):
    MENU_SELECTOR = '//span[text()="{}"]'
    PROCEED_BUTTON = (By.ID, 'reset-button')
    SIDE_MENU = (By.CLASS_NAME, 'in-sidebar-wrapper__routes')
    SIDE_MENU_ITEMS = (By.CLASS_NAME, 'in-sidebar-wrapper__groups')
    OPTIMIZE = (By.XPATH, MENU_SELECTOR.format("Optimize"))
    INSTORY = (By.XPATH, MENU_SELECTOR.format("InStory"))
    PARTNER_PAGE_LOGO = (By.CLASS_NAME, 'in-sidebar-wrapper__logo name')
    PARTNER_PAGE_GRAPHS = (By.ID, 'custom-line')
    PARTNER_BAR_CHART = (By.ID, 'bar-chart')

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait_for_element_visible(self.SIDE_MENU_ITEMS, "Partner logo is not visible")
        self.wait_for_element_visible(self.PARTNER_PAGE_GRAPHS, "Graphs is not visible in Partner page")
        self.wait_for_element_visible(self.PARTNER_BAR_CHART, "Bar chart is not visible in Partner page")

    def select_experience_on_side_menu(self):
        self.wait_for_element_clickable(self.SIDE_MENU_ITEMS)
        self.wait_for_element_clickable(self.find_elements(2, *self.SIDE_MENU_ITEMS)).click()
        self.select_experience_sub_menu_items()
        return InstoryPage(self.driver)

    def select_experience_sub_menu_items(self):
        self.wait_for_element_clickable(self.OPTIMIZE).click()
        self.select_optimize_sub_menu_items()

    def select_optimize_sub_menu_items(self):
        self.click(*self.INSTORY)