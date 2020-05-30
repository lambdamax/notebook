from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class AutoTest:
    def __init__(self):
        """
        Run cmd before class init
        chrome.exe  --remote-debugging-port=9222 --user-data-dir="D:\setup\selenum\AutomationProfile"
        """
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def await_by_page(self, xpath, by=By.XPATH):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, xpath))
        )

    def login(self):
        url = 'https://dmsplus-training.essilorchina.com/web/login'
        self.driver.get(url)
        self.await_by_page("login", By.ID)
        js = 'document.getElementById("loginButton").removeAttribute("disabled")'
        self.driver.execute_script(js)
        self.driver.find_element_by_id('login').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('admin')
        self.driver.find_element_by_id('loginButton').click()

    def select_ws_inventory(self):
        url = 'https://dmsplus-training.essilorchina.com/web#action=338&model=entity.line&view_type=kanban&menu_id=205'
        self.driver.get(url)
        self.await_by_page('/html/body/div[1]/main/div[2]/div/div/div[2]/div[2]/div[3]/ul/li[2]/button')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/main/div[2]/div/div/div[2]/div[2]/div[3]/ul/li[2]/button').click()
        WebDriverWait(self.driver, 5).until(
            EC.url_changes(
                'https://dmsplus-training-ws.essilorchina.com/web#action=100&active_id=mailbox_inbox&menu_id=77')
        )

        url = 'https://dmsplus-training-ws.essilorchina.com/web#action=187&model=stock.inventory&view_type=list&menu_id=111'
        self.driver.get(url)
        self.await_by_page('/html/body/div[1]/main/div[1]/div[2]/div/div/button[1]')

    def create_ws_inventory(self):
        pass
        self.driver.find_element_by_xpath('//button[@accesskey="c"]').click()
        self.await_by_page('//input[@name="inventory_reason"]')
        self.driver.find_element_by_xpath('//input[@name="inventory_reason"]').send_keys('test')
        product = self.driver.find_element_by_xpath('//div[@name="product_tmpl_id"]//input')
        product.click()
        product.send_keys('UAV100606B')
        time.sleep(1.5)
        product.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//button[@name="action_start"]').click()
        self.await_by_page('//button[@name="enter_manually"]')
        self.driver.find_element_by_xpath('//button[@accesskey="a"]').click()

    def run(self):
        self.login()
        self.select_ws_inventory()
        self.create_ws_inventory()


if __name__ == '__main__':
    t = AutoTest()
    t.run()
    input('done')
