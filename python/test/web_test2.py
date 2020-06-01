from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class AutoTest:
    def __init__(self, path):
        """
        Run cmd before class init
        chrome.exe  --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
        """
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.barcodes = []
        with open(path, 'r') as f:
            for line in f.readlines():
                self.barcodes.append(line)

    def parse(self):
        for index, barcode in enumerate(self.barcodes):
            self.driver.find_element_by_xpath('/html/body').send_keys(barcode)
            print('第 %s 个码: %s' % (index, barcode.replace('\n', '')))
            time.sleep(0.5)


if __name__ == '__main__':
    path = r'C:\Users\yaorh\Desktop\ee.txt'
    t = AutoTest(path)
    t.parse()
    print('Done')
