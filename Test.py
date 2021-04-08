from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = r"C:\Users\petit\Documents\chromedriver" ##insert path here

destination = input("Please enter desired URL: (without https://)")

driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("https://" + destination)

driver.maximize_window()