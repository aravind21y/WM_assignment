from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://dev.workmarket.com/login")

login = driver.find_element_by_id("login-email")
login.send_keys("test12345@workmarket.com")

pwd = driver.find_element_by_id("login-password")
pwd.send_keys("candidate")

login_button = driver.find_element_by_class_name('mdl-button__ripple-container').click()

assert 'Invalid user name or password.' in driver.page_source 

time.sleep(2)

driver.find_element_by_id("login-email").clear()
driver.find_element_by_id("login-email").send_keys("qatest123@workmarket.com")
forgot_pwd = driver.find_element_by_id("reset-password").click()
reset_submit = driver.find_element_by_id("reset-submit").click()

assert 'If we have your email address on file, we\'ve sent you password reset instructions.' in driver.page_source 

time.sleep(2)

driver.find_element_by_id("login-email").clear()
driver.find_element_by_id("login-email").send_keys("qa+candidatetest@workmarket.com")

driver.find_element_by_id("login-password").send_keys("candidate123")
driver.find_element_by_class_name('mdl-button__ripple-container').click()

assert 'reCAPTCHA response is required' in driver.page_source 
assert 'You have entered the wrong password too many times and your account has been locked. Please reset your password to unlock your account' in driver.page_source 
