from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from pathlib import Path


class lazadaPage:
    # take comment one of them ==

    # For Windows
    CHROME_PATH = str(Path().absolute())+'/tools/chromedriver.exe'
    # For Linux
    # CHROME_PATH = str(Path().absolute())+'tools/chromedriver'

    # end of take comment
    url = ""
    link = []

    def __init__(self, url):
        self.url = url
        self.link = []
        self.driver = webdriver.Chrome(self.CHROME_PATH)

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
