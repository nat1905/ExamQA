from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

class TestHovers(unittest.TestCase):
    """hovers
        http://the-internet.herokuapp.com/hovers"""

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.accept_insecure_certs = True
        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.base_url = "http://the-internet.herokuapp.com/hovers"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(5)
        self.assertIn(self.base_url, self.driver.current_url)


    def test_hovers1(self):
        """test_hovers_one"""

        driver = self.driver
        element_to_hover_over = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(3) > img:nth-child(1)")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(5)
        name_user1 = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(3) > div:nth-child(2) > h5:nth-child(1)")
        self.assertTrue(name_user1)
        time.sleep(5)
        view_profile1 = self.driver.find_element(By.CSS_SELECTOR,"div.figure:nth-child(3) > div:nth-child(2) > a:nth-child(2)")
        self.assertTrue(view_profile1)
        time.sleep(5)
        driver.save_screenshot("hover1.png")

    def test_hovers2(self):
        """test_hovers_two"""

        driver = self.driver
        element_to_hover_over = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(4) > img:nth-child(1)")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(5)
        name_user2 = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(4) > div:nth-child(2) > h5:nth-child(1)")
        self.assertTrue(name_user2)
        time.sleep(5)
        view_profile2 = self.driver.find_element(By.CSS_SELECTOR,"div.figure:nth-child(4) > div:nth-child(2) > a:nth-child(2)")
        self.assertTrue(view_profile2)
        time.sleep(5)
        driver.save_screenshot("hover2.png")

    def test_hovers3(self):
        """test_hovers_three"""

        driver = self.driver
        element_to_hover_over = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(5) > img:nth-child(1)")
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(5)
        name_user3 = self.driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(5) > div:nth-child(2) > h5:nth-child(1)")
        self.assertTrue(name_user3)
        time.sleep(5)
        view_profile3 = self.driver.find_element(By.CSS_SELECTOR,"div.figure:nth-child(5) > div:nth-child(2) > a:nth-child(2)")
        self.assertTrue(view_profile3)
        time.sleep(5)
        driver.save_screenshot("hover3.png")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

