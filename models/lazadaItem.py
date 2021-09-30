from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


class lazadaItem:
    url = ""
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = uc
    content = ""
    images = []

    def __init__(self, url):
        self.url = url
        self.content = ''
        self.images = []
        self.driver = uc.Chrome(options=self.options)

    def getData(self):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 1500);')
            time.sleep(5)
            contenth = self.driver.execute_script(
                'return document.querySelector("body > script:nth-child(6)").text')
            self.content = contenth.replace('\n', '')

        except TimeoutException:
            return f" Error Timeout"

        return self.content

    def getImage(self):
        try:
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 2500);')
            time.sleep(5)
            image = self.driver.find_elements(
                By.CLASS_NAME, value='item-gallery__thumbnail-image')
            for a in image:
                self.images.append(a.get_attribute('src'))

        except TimeoutException:
            return f" Error Timeout"

        return self.images

    def shutDown(self):
        self.driver.quit()
