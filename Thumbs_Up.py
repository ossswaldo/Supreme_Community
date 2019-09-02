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
        #options.add_argument('incognito')
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/BigO/Documents/CODE/Supreme_Community/chromedriver')

    def execute(self):
        self.setupselenium()
        self.discord()
        self.cleanUpBrowser()


    def discord(self):
        self.driver.get('https://discordapp.com/channels/')

        print(datetime.now(),'Discord Launched, Searching For Fields.')
        inputElement = self.driver.find_element_by_xpath("//*[@type='email']")
        inputElement.send_keys('arguetaoswaldo@yahoo.com')
        print(datetime.now(),'Typing in email bar')

        inputElement = self.driver.find_element_by_xpath("//*[@type='password']")
        inputElement.send_keys('playa0976')
        print(datetime.now(),'Typing in password bar')


        wait = WebDriverWait(self.driver, 10)
        on = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@type='submit']")))
        ActionChains(self.driver).move_to_element(on).click().perform()

        time.sleep(3)
        chat = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@aria-label,'HeraMemon')]")))
        ActionChains(self.driver).move_to_element(chat).click().perform()

        counter = 0
        while counter<10:
            inputElement = self.driver.find_element_by_xpath("//*[@placeholder='Message @HeraMemon']")
            inputElement.send_keys('@HeraMemon whats good.')
            inputElement.send_keys('\n')
            print(datetime.now(),'Typing in chat bar',counter,"times" )
            counter+= 1

            if counter % 10 == 0:
                time.sleep(2)



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
