from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = r"C:\Users\petit\Documents\chromedriver" ##insert path here

###destination = input("Please enter desired URL: ")

driver = webdriver.Chrome(PATH)


driver.get("https://pornhub.com")


searchbar = driver.find_element_by_name("search")
searchbar.send_keys("Cowgirl" + Keys.RETURN)
driver.maximize_window()

vid = driver.find_element_by_xpath('/html/body/div[6]/div/div[5]/div/div/ul/li[2]/div/div[1]/a')
vid.click()

driver.maximize_window()

full = driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/div[1]/div[1]/div[1]/div[1]/video-element')
sleep(3)
full.click()
full.click()