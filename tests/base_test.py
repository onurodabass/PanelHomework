import logging
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = "https://seleniumautomation.inone.useinsider.com/"

    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-notifications')
        option.add_argument('--allow-running-insecure-content')
        option.add_argument('--headless')
        option.add_argument("--remote-debugging-port=9222")
        option.add_argument("window-size=1280x800")
        option.binary_location = '/usr/bin/google-chrome'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(45)
        self.logger = logging.getLogger()

    def tearDown(self):
        self.driver.close()
