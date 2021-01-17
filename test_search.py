import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver

exec_path = 'C:\Drivers\chromedriver.exe'

class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()

    @allure.feature('Open pages')
    @allure.story('Открываем страницу https://www.google.ru/')
    @allure.severity('Blocker')
    def test_google_search(self):
        self.driver.get('https://www.google.ru/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу https://www.yandex.ru/')
    @allure.severity('Critical')
    def test_yandex_search(self):
        self.driver.get('https://www.yandex.ru/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Яндекс'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу https://www.mail.ru/')
    @allure.severity('Trivial')
    def test_yahoo_search(self):
        self.driver.get('https://www.mail.ru/')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Mail.ru: почта, поиск в интернете, новости, игры'