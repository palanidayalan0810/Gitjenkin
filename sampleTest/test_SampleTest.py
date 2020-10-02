import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure


class TestGitHub:
    driver=None
    @allure.description("This test case is for validating google")
    @allure.severity(severity_level="critical")
    def test_Sample1(self):
        try:
            self.driver=webdriver.Chrome("C:\\Users\\dell\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
            self.driver.get("https://www.google.com/")
            input=self.driver.find_element_by_name("q")
            input.send_keys('chennai')
            input.send_keys(Keys.ENTER)

        finally:
            allure.attach(self.driver.get_screenshot_as_png(), name="Google",
                          attachment_type=allure.attachment_type.PNG)


    @allure.description("This test case is for validating bing")
    @allure.severity(severity_level="normal")
    def test_Sample2(self):
        try:
            self.driver = webdriver.Chrome("C:\\Users\\dell\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
            self.driver.get("https://www.bing.com/")
            input = self.driver.find_element_by_name("q")

            input.send_keys('chennai')
            input.send_keys(Keys.ENTER)
            input = self.driver.find_element_by_name("qaaaas")

        finally:
            allure.attach(self.driver.get_screenshot_as_png(), name="Bing",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.fixture()
    def setup(self):
        print("im setup function")

        yield
        allure.attach(self.driver.get_screenshot_as_png(), name="sample", attachment_type=allure.attachment_type.PNG)

