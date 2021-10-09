from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import undetected_chromedriver as uc
from pathlib import Path


class lazadaPage:
    # For Windows
    CHROME_PATH = str(Path().absolute())+'/tools/chromedriver.exe'
    # For Linux
    # CHROME_PATH = str(Path().absolute())+'tools/chromedriver'
    url = ""
    link = []
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    uc.install(
        executable_path=CHROME_PATH,
    )
    driver = uc

    def __init__(self, url):
        self.url = url
        self.link = []
        self.driver = uc.Chrome(options=self.options)

    def getPage(self):
        try:
            self.driver.get(self.url)
            time.sleep(7)
            self.driver.execute_script('window.scrollTo(0, 1500);')
            time.sleep(7)
            self.driver.execute_script('window.scrollTo(0, 2500);')
            time.sleep(7)
            soup_b = BeautifulSoup(self.driver.page_source, 'html.parser')
            produc = soup_b.find('div', class_='_1Ffv-')
            prd = produc.find_all('div', class_='_1MFo_')
            for lins in prd:
                plink = lins.find_all('a')
                for pl in plink:
                    self.link.append(pl.get('href').replace(
                        '//www.lazada.co.id', 'https://lazada.co.id').replace('?mp=1&freeshipping=1', ''))

        except TimeoutException:
            print(" ERROR TIMEOUT")

        print(len(self.link))
        return self.link

    def shutDown(self):
        self.driver.quit()
