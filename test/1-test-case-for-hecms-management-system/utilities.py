import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

test_folder = ""

# Set ChromeDriver path
chromedriver_path = 'assets/chromedriver'

# Create Chrome webdriver
driver = webdriver.Chrome(chromedriver_path)

# Maximize the window
driver.maximize_window()

# Navigate to hecms.local
driver.get('http://hecms.local')

# Do something with the website...


def test_super_admin_password_failed():
	# Find the username field by name and enter the value
	username_field = driver.find_element(By.NAME, 'username')
	username_field.send_keys('your_username')

	# Find the password field by name and enter the value
	password_field = driver.find_element(By.NAME, 'password')
	password_field.send_keys('your_password')

	# Find the account_type select element by name and select "Super Admin" option
	account_type_select = Select(driver.find_element(By.NAME, 'account_type'))
	account_type_select.select_by_visible_text('Super Admin')

	# Find the login button by name and click it
	login_button = driver.find_element(By.NAME, 'login')
	login_button.click()
	# Take a screenshot and save it to a file
	screenshot_file = f"{test_folder}/screenshots/0-login-failed-test.png"
	driver.save_screenshot(screenshot_file)

