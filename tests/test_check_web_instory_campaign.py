import time


from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestCheckWebInstoryCampaign(BaseTest):
    email = "onur.odabas@useinsider.com"
    password = "549379Fener."
    condition = "Page Type"
    operator = "is"
    language = "All Languages"
    page_condition = "All Pages"
    activation_time = "Never Ends"
    activation_status = "Test"
    selected_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    rules = "Page Type is All Pages"
    priority = "10"
    note = "OnurTest"
    campaign_status = "Visible"


    def test_check_web_instory_campaign(self):
        login_page = LoginPage(self.driver)
        login_page.fill_login_form(self.email, self.password)
        partner_page = login_page.click_login_button()

        campaign_name = partner_page.generate_campaign_name()
        instory_page = partner_page.select_experience_on_side_menu()
        instory_page.create_desktop_campaign(campaign_name)

        rules_page = instory_page.add_rule_to_campaign()
        rules_page.select_condition(self.condition).select_operator(self.operator)
        design_pages = rules_page.click_save_and_continue()
        action_builder_page = design_pages.click_add_new_variant()
        time.sleep(5)
        action_builder_page.hover_template()
        action_builder_page.select_instory_template()
        action_builder_page.click_ok_button()
        action_builder_page.click_insert_before_element()
        time.sleep(3)
        action_builder_page.click_save_button()
        time.sleep(5)
        instory_page.click_save_and_continue()
        time.sleep(5)
        instory_page.click_save_and_continue()
        instory_page.select_personalization_language(self.language)
        time.sleep(2)
        instory_page.change_activation_time('00:30')
        instory_page.change_display_settings('Monday')
        instory_page.change_priority(self.priority)
        instory_page.change_activation_status(self.activation_status)
        instory_page.add_note(self.note)
        instory_page.launch_campaign()
        time.sleep(5)
        instory_page.generate_campaign()
        instory_page.search_campaign(campaign_name)
        instory_page.get_campaign_status()
        instory_page.test_link_is_present()
        instory_page.go_to_campaign_details()
        self.assertEqual(campaign_name, instory_page.get_campaign_name(), "ok değil")
        self.assertEqual(self.priority, instory_page.get_campaign_priority(), "ok değil")
        self.assertEqual(self.rules, instory_page.get_campaign_rules(), "ok değil")
        self.assertEqual(self.note, instory_page.get_capaign_note(), "ok değil")
        campaign_id = instory_page.get_campaign_id()
        instory_page.close_detail_side_menu()
        instory_page.click_test_link()
        instory_page.go_to_test_link()
        instory_page.is_present_campaign_class(campaign_id)
        instory_page.partner_page_campaign_control(campaign_id)