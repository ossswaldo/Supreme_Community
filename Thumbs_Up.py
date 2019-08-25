from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#from easygui import*


from datetime import datetime
import time


class ChangeTheMarket():

    def __init__(self):
        self.driver = None

    def setupselenium(self):
        options = Options()
        #options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('ignore-certificate-errors')
        options.add_argument('incognito')
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/BigO/Documents/CODE/Supreme_Community/chromedriver')

    def execute(self):
        self.setupselenium()
        self.openUpBrowser()
        #self.cleanUpBrowser()

    def openUpBrowser(self):
        print(datetime.now(),'Supreme Community Script Initiated -')
        self.driver.get('https://www.supremecommunity.com/season/fall-winter2019/droplist/2019-08-22/')
        self.driver.delete_all_cookies()
        print(datetime.now(),'Openeing supremecommunity.com')

    def cleanUpBrowser(self):
        print(datetime.now(),'Quitting Browser')
        self.driver.quit()


if __name__== "__main__":
    taskMaster =  ChangeTheMarket()
    taskMaster.execute()
