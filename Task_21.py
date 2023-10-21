from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Task19:
   
   username = "standard_user"
   password = "standard_user"
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
       print("Cookies before login:")
       for cookie in self.driver.get_cookies():
        print(f"{cookie['name']}: {cookie['value']}")
       self.driver.maximize_window()
       self.driver.get(self.url)
       print(self.driver.title)
       print(self.driver.current_url)
       sleep(2)
       self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
       sleep(2)
       self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
       sleep(2)
       self.driver.find_element(by=By.ID, value="login-button").click()
       print("Cookies after login:")
       for cookie in self.driver.get_cookies():
        print(f"{cookie['name']}: {cookie['value']}")
       
   def shutdown(self):
       self.driver.quit()




url = "https://www.saucedemo.com/"


task = Task19(url)


task.login()


task.shutdown()

