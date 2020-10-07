from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from operator import itemgetter

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('http://zzzscore.com/1to50/en/')


elements = driver.find_elements_by_xpath('//*[@id="grid"]/div')
ordered_elements = sorted(((int(element.text), element) for element in elements), key=itemgetter(0))
for value, element in ordered_elements:
    element.click()


elements = driver.find_elements_by_xpath('//*[@id="grid"]/div')
ordered_elements = sorted(((int(element.text), element) for element in elements), key=itemgetter(0))
for value, element in ordered_elements:
    element.click()
