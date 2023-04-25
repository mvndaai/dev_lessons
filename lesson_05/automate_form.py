# https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
# pip3 install webdriver-manager
# Note: CSS slectors # is id, . is class

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost:5500/lesson_03/form.html")
print('Title:', driver.title)
assert(driver.title == 'Form')
time.sleep(3) # wait before changing anything

driver.find_element(By.ID, 'text').send_keys('Test Name')
el_num = driver.find_element(By.XPATH, '//input[@name="number"]')

el_num.clear()
el_num.send_keys('7')

select = Select(driver.find_element(By.ID, 'select'))
print('original selected value:', select._el.get_attribute('value'))
select.select_by_value('C')
time.sleep(1) # wait before changing another
select.select_by_visible_text('Alpha')

driver.find_element(By.CSS_SELECTOR, '#radio_false').click()

time.sleep(1) # wait befor changing page
driver.find_element(By.ID, 'form').submit()

time.sleep(10) # wait before closing