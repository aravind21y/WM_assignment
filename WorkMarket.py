from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://dev.workmarket.com/login")

login = driver.find_element_by_id("login-email")
login.send_keys("qa+candidatetest@workmarket.com")

pwd = driver.find_element_by_id("login-password")
pwd.send_keys("candidate123")

login_button = driver.find_element_by_class_name('mdl-button__ripple-container').click()

find_talent = driver.find_element_by_xpath("//header[@id='wm-main-nav']/div/div/div/div/div[2]/div[2]/a/div/div/div").click()
search = driver.find_element_by_id('input-text')
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(2)

# length of results is currently hardcoded (50), it's best to use the len method to count through the profile-card elements  
for i in range(0, 50):
    results1 = driver.find_elements_by_class_name('profile-card')[i].text

    assert  ('Test' or 'test' in results1)

#AssertionError will display if "test" string is not found in each element