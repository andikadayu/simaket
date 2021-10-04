"""
 Copyright 2021 Andika Dayu.
 SPDX-License-Identifier: Apache-2.0
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from pathlib import Path


class shopeePage:
    # take comment one of them ==

    # For Windows
    CHROME_PATH = str(Path().absolute())+'/tools/chromedriver.exe'
    # For Linux
    # CHROME_PATH = str(Path().absolute())+'tools/chromedriver'

    # end of take comment

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('log-level=2')
    url = ""
    numberMaxPage = 0
    links = []

    def __init__(self, url):
        self.url = url
        self.links = []
        self.driver = webdriver.Chrome(self.CHROME_PATH)

    def getMaxPage(self):
        try:
            self.driver.get('https://shopee.co.id/shop/'+self.url+'/search')
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 1500);')
            time.sleep(5)
            self.driver.execute_script('window.scrollTo(0, 2500);')
            time.sleep(5)
            soup_a = BeautifulSoup(self.driver.page_source, 'html.parser')
            pages = soup_a.find(
                'span', class_='shopee-mini-page-controller__total')

            for pag in pages:
                self.numberMaxPage = pag

        except TimeoutException:
            return f"==Error Timeout=="

        return self.numberMaxPage

    def getAllUrl(self, number):
        # Limiter
        # rn = 34 if number >= 34 else int(number)
        i = 0

        while(i < int(number)):
            try:
                self.driver.get('https://shopee.co.id/shop/' +
                                self.url + "/search?page={}&sortBy=pop".format(i))
                time.sleep(5)
                self.driver.execute_script('window.scrollTo(0, 1500);')
                time.sleep(5)
                self.driver.execute_script('window.scrollTo(0, 2500);')
                time.sleep(5)
                soup_a = BeautifulSoup(self.driver.page_source, 'html.parser')
                products = soup_a.find(
                    'div', class_='shop-search-result-view')
                prs = products.find_all('a')
                for link in prs:
                    self.links.append(link.get('href'))

            except TimeoutException:
                return f"==Error Timeout=="

            i += 1

        return self.links

    def shutDown(self):
        self.driver.quit()
