import time
from itertools import cycle

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('http://zzzscore.com/dontap/en/')

time.sleep(1)

my = element = driver.find_element_by_css_selector('#grid > div:nth-child(3)').rect['y']

for index in cycle(range(1, 5+1)):
    while True:
        element = driver.find_element_by_css_selector(f'#grid > div:nth-child({index}) > div.tab.b')

        y = element.rect['y'] + element.rect['height']

        print(my, y)

        if y > my:
            element.click()
            break
