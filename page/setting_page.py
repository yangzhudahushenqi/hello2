from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure

class SettingPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"

    @allure.step(title="点击放大镜")
    def click_search(self):
        self.click(self.search_button)