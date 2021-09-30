import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
import json
from selenium.webdriver.common.by import By
from selenium import webdriver


class lazadaPage:
    url = ""
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = uc
    link = []

    def __init__(self, url):
        self.url = url
        self.link = []
        self.driver = uc.Chrome(options=self.options)

    def getPage(self):
        try:
            self.driver.get(self.url)
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 1500);')
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 2500);')
            time.sleep(5)
            soup_b = BeautifulSoup(self.driver.page_source, 'html.parser')
            produc = soup_b.find('div', class_='_1Ffv-')
            prd = produc.find_all('a', class_='_28YRT')
            for lins in prd:
                if "https://lazada.co.id"+lins.get('href') not in self.link:
                    self.link.append('https://lazada.co.id'+lins.get('href'))

        except TimeoutException:
            print(" ERROR TIMEOUT")

        print(len(self.link))
        return self.link

    def shutDown(self):
        self.driver.quit()
