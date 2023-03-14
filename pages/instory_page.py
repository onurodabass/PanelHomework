import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.action_builder_page import ActionBuilderPage
from pages.base_page import BasePage


class InstoryPage(BasePage):
    CREATE_BUTTON = (By.ID, 'create-mobile-campaign')
    CAMPAIGN_NAME_TEXT_BOX = (By.ID, 'campaign-name')
    PLATFORM_TYPE = "//button[@value='{}']"
    DESKTOP = (By.XPATH, PLATFORM_TYPE.format("web"))
    ACCEPT_BUTTON = (By.ID, 'accept')
    PAGE_RULES = (By.XPATH, './/*[contains(@class, "page-rules")]')
    CONDITION_LIST = (By.ID, 'conditionList0')
    CONDITION_SEARCH_BOX = (By.ID, 'conditionList0-search')
    OPERATOR_LIST = (By.ID, 'operatorList0')
    OPERATOR_SELECTION = "//*[contains(@class, 'in-dropdown')]//a[text() = ' {} ']"
    SAVE_AND_CONTINUE_BTN = (By.ID, 'save-and-next')
    ADD_NEW_VARIANT_BTN = (By.ID, 'add-new-variation')
    LANGUAGE_LIST = (By.ID, 'personalization-language')
    HOUR_TAB = (By.XPATH, '//*[@name="startHour"]')
    TEXT_SELECTOR = '//*[contains(text(), "{}")]'
    DISPLAY_SETTINGS = (By.XPATH, './/*[contains(@class, "qa-accordion")]//p[contains(text(), "DISPLAY SETTINGS")]')
    WHEN_ACTIVE_DAYS = (By.XPATH, "//*[@for = 'When active, display the personalization only on selected days.']")
    ADVANCE_SETTINGS = (By.XPATH, './/*[contains(@class, "qa-accordion")]//p[contains(text(), " Advanced Settings ")]')
    PRIORITY = (By.ID, 'priority')
    PRIORITY_SELECT = 'priority-{}'
    BODY = (By.TAG_NAME, 'body')
    FOR_SELECTOR = '//*[@for = "{}"]'
    CAMPAIGN_DETAILS = (By.XPATH, "//*[contains(@class, 'vuetable-body')]//*[contains(text(), 'Details')]")
    NOTE_TEXT_BOX = (By.ID, 'note')
    LAUNCH_CAMPAIGN = (By.ID, 'save-and-next')
    SEARCH_INPUT = (By.ID, 'search-value')
    CAMP_STATUS = (By.XPATH, './/*[contains(@class, "camp-status")]')
    TEST_LINK = (By.XPATH, '//td[contains(@class, "test-link")]')
    CAMP_NAME = (By.CLASS_NAME, 'in-modal-wrapper__title')
    CAMP_PRIORITY = (By.ID, 'priority-value')
    CAMP_RULES = (By.CLASS_NAME, 'personalization-rule-0')
    CAMP_NOTE = (By.CLASS_NAME, 'personalization-note')
    DETAIL_CLOSE = (By.CLASS_NAME, 'qa-close')
    TEST_LINK_VARIATION_GROUP_BTNS = (By.CSS_SELECTOR, '.in-box .clearfix')
    TEST_LINK_DOMAIN_URL = (By.CSS_SELECTOR, '.in-box .clearfix a')
    USER_SETTINGS = (By.CSS_SELECTOR, 'li:nth-child(6) > a')
    GENERATE = (By.LINK_TEXT, 'Generate')
    CAMPAIGN_VISIBILITY = (By.CLASS_NAME, 'inspector-personalization-visible')
    CAMPAIGN_ID = (By.CSS_SELECTOR, 'td.personalization-id span')
    CAMPAIGN_CLASS = '//div[contains(@class, "{}")]'

    def __init__(self, driver):
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.CREATE_BUTTON) else False

    def create_desktop_campaign(self, campaign_name):
        self.click(*self.CREATE_BUTTON)
        self.fill_campaign_name(campaign_name)

    def fill_campaign_name(self, campaign_name):
        self.fill(campaign_name, *self.CAMPAIGN_NAME_TEXT_BOX)
        self.select_desktop_platform()
        self.create_campaign_button()

    def select_desktop_platform(self):
        self.click(*self.DESKTOP)

    def create_campaign_button(self):
        self.click(*self.ACCEPT_BUTTON)

    def add_rule_to_campaign(self):
        self.navigate_tabs("Rules")
        time.sleep(4)
        self.wait_for_element_clickable(self.PAGE_RULES).click()
        return self

    def check_campaign_rules(self, condition, operator):
        if self.find_element(*self.CONDITION_LIST).text == condition and self.find_element(
                *self.OPERATOR_LIST).text == operator:
            return True

    def navigate_tabs(self, tab_name):
        self.click(By.LINK_TEXT, '{}'.format(tab_name))

    def select_condition(self, condition):
        self.click(*self.CONDITION_LIST)
        self.fill(condition, *self.CONDITION_SEARCH_BOX).fill(Keys.ENTER, *self.CONDITION_SEARCH_BOX)
        return self

    def select_operator(self, operator):
        self.click(*self.OPERATOR_LIST)
        self.click(By.XPATH, self.OPERATOR_SELECTION.format(operator))

    def click_save_and_continue(self):
        time.sleep(1)
        self.wait_for_element_clickable(self.SAVE_AND_CONTINUE_BTN).click()
        return self

    def click_add_new_variant(self):
        self.click(*self.ADD_NEW_VARIANT_BTN)
        return ActionBuilderPage(self.driver)

    def select_personalization_language(self, language):
        self.click(*self.LANGUAGE_LIST)
        self.click(By.LINK_TEXT, language)

    def change_activation_time(self, activation_time):
        self.wait_for_element_clickable(self.HOUR_TAB).click()
        self.wait_for_element_clickable((By.XPATH, self.TEXT_SELECTOR.format(activation_time))).click()

    def change_display_settings(self, *days):
        self.scroll(*self.BODY)
        time.sleep(1)
        self.wait_for_element_clickable(self.DISPLAY_SETTINGS).click()
        time.sleep(2)
        self.wait_for_element_clickable(self.WHEN_ACTIVE_DAYS).click()
        for day in days:
            self.wait_for_element_clickable((By.XPATH, self.FOR_SELECTOR.format(day))).click()

    def change_priority(self, priority):
        self.scroll(*self.BODY)
        time.sleep(1)
        self.wait_for_element_clickable(self.ADVANCE_SETTINGS).click()
        time.sleep(2)
        self.wait_for_element_clickable(self.PRIORITY).click()
        self.wait_for_element_clickable((By.CLASS_NAME, self.PRIORITY_SELECT.format(priority))).click()

    def change_activation_status(self, status):
        self.wait_for_element_clickable((By.XPATH, self.FOR_SELECTOR.format(status))).click()

    def add_note(self, note):
        self.fill(note, *self.NOTE_TEXT_BOX)

    def launch_campaign(self):
        self.wait_for_element_clickable(self.LAUNCH_CAMPAIGN).click()

    def search_campaign(self, name):
        self.wait_for_element_clickable(self.SEARCH_INPUT)
        self.fill(name, *self.SEARCH_INPUT)
        time.sleep(2)

    def get_campaign_status(self):
        return self.wait_for_element_visible(self.CAMP_STATUS).text

    def test_link_is_present(self):
        return self.wait_for_element_clickable(self.TEST_LINK)

    def go_to_campaign_details(self):
        self.wait_for_element_clickable(self.CAMPAIGN_DETAILS).click()
        return self

    def get_campaign_name(self):
        return self.wait_for_element_visible(self.CAMP_NAME).text

    def get_campaign_priority(self):
        return self.wait_for_element_visible(self.CAMP_PRIORITY).text

    def get_campaign_rules(self):
        return self.wait_for_element_visible(self.CAMP_RULES).text

    def get_capaign_note(self):
        return self.wait_for_element_visible(self.CAMP_NOTE).text

    def close_detail_side_menu(self):
        self.click(*self.DETAIL_CLOSE)

    def click_test_link(self):
        time.sleep(1)
        self.wait_for_element_clickable(self.TEST_LINK).click()

    def go_to_test_link(self):
        self.wait_for_element_clickable(self.TEST_LINK_VARIATION_GROUP_BTNS)
        self.hover(self.find_elements(0, *self.TEST_LINK_VARIATION_GROUP_BTNS))
        self.driver.get(self.find_elements(0, *self.TEST_LINK_DOMAIN_URL).get_attribute('href'))
        return self

    def generate_campaign(self):
        i = 0
        while i < 3:
            self.wait_for_element_clickable(self.USER_SETTINGS).click()
            self.wait_for_element_clickable(self.GENERATE).click()
            time.sleep(11)
            i = i + 1

    def get_campaign_visibility(self):
        return self.wait_for_element_visible(self.CAMPAIGN_VISIBILITY).text

    def get_campaign_id(self):
        return self.find_elements(0, *self.CAMPAIGN_ID).text

    def is_present_campaign_class(self, campaign_id):
        return self.wait_for_element_clickable((By.XPATH, self.CAMPAIGN_CLASS.format(campaign_id)))

    def partner_page_campaign_control(self, campaign_id):
        time.sleep(2)
        camp_local_storage = self.driver.execute_script("return spApi.storageData('sp-camp-{}')".format(campaign_id))
        if camp_local_storage:
            return camp_local_storage
        else:
            return ''