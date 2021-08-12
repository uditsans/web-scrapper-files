import time
import json

from selenium import webdriver
from selenium.webdriver.chrome import service

from parsel import Selector

f = open('github_pass.json', 'r')
keys = dict(json.load(f))
f.close()

webdriver_service = service.Service('./webdrivers/operadriver')
webdriver_service.start()

browser = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
browser.maximize_window()
browser.get('https://github.com/')
time.sleep(1)

signin = browser.find_element_by_xpath('//*[contains(text(), "Sign in")]')
signin.click()

username = browser.find_element_by_xpath('//*[@id="login_field"]')
username.click()
username.send_keys(keys['username'])

password = browser.find_element_by_xpath('//*[@id="password"]')
password.click()
password.send_keys(keys['password'])
time.sleep(1)

signin = browser.find_element_by_xpath('//*[contains(@value, "Sign in")]')
signin.click()
time.sleep(1)

links = browser.find_element_by_xpath('//*[contains(@aria-label, "View profile and more")]')
links.click()
time.sleep(1)

logout = browser.find_element_by_xpath('//*[contains(text(), "Sign out")]')
logout.click()

time.sleep(2)
browser.close()
