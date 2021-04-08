from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

os.system("cls")

PATH = r"C:\Users\petit\Documents\chromedriver" ##insert path here

destination = input("Please enter desired URL: (without https://)")

driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get("https://" + destination)

driver.maximize_window()

os.system("cls")

print("Opened: https://" + destination)