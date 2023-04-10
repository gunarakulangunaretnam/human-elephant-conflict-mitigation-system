import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def test_super_admin_login_failed():

	try:
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
		screenshot_file = f"{test_folder}/screenshots/0-device-admin-login-failed-test.png"
		driver.save_screenshot(screenshot_file)
		
		return True

	except Exception as e:
		return False

		
def test_super_admin_password_passed():

	try:
		# Find the username field by name and enter the value
		username_field = driver.find_element(By.NAME, 'username')
		username_field.send_keys('admin')

		# Find the password field by name and enter the value
		password_field = driver.find_element(By.NAME, 'password')
		password_field.send_keys('admin')

		# Find the account_type select element by name and select "Super Admin" option
		account_type_select = Select(driver.find_element(By.NAME, 'account_type'))
		account_type_select.select_by_visible_text('Super Admin')

		# Find the login button by name and click it
		login_button = driver.find_element(By.NAME, 'login')
		login_button.click()
		# Take a screenshot and save it to a file
		screenshot_file = f"{test_folder}/screenshots/1-super-admin-login-passed-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_home_page_open():

	try:

		link = driver.find_element(By.LINK_TEXT, 'Home Page')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/2-super-admin-home-page-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True
	except Exception as e:
		return False


def test_super_admin_home_page_filter():

	try:
		month_picker = driver.find_element(By.ID, 'month_picker')
		month_picker.click()
		month_picker.send_keys('2023-03')

		screenshot_file = f"{test_folder}/screenshots/3-super-admin-home-page-filter-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False

def test_super_admin_data_management_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Data Management')
		link.click()

		# Scroll down the page
		driver.execute_script("window.scrollBy(0, 1000)")

		# Scroll up the page
		driver.execute_script("window.scrollBy(0, -1000)")

		screenshot_file = f"{test_folder}/screenshots/4-super-admin-data-management-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_data_management_show_all_data_function():

	try:
		# Find the login button by name and click it
		radio_btn = driver.find_element(By.ID, 'show_all_data')
		radio_btn.click()

		screenshot_file = f"{test_folder}/screenshots/5-super-admin-data-management-show-all-data-function-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_data_management_date_wise_search_function():

	try:

		# Find the login button by name and click it
		radio_btn = driver.find_element(By.ID, 'search_by_date')
		radio_btn.click()

		# Find the login button by name and click it
		date_picker = driver.find_element(By.ID, 'date_picker')
		date_picker.click()
		# Send a date string to the date picker input element
		date_value = "2023-04-10" # Set the date value that you want to enter
		driver.execute_script("arguments[0].value = arguments[1];", date_picker, date_value)

		screenshot_file = f"{test_folder}/screenshots/6-super-admin-data-management-date-search-function-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_device_management_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Device Management')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/7-super-admin-device-management-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_device_management_create_a_device_function():

	try:
		# Find the button element
		button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='+Add New Device']")))
		button.click()

		time.sleep(2)

		# Find the form fields and enter sample data
		driver.find_element(By.ID, "deviceName").send_keys("Sample Name")
		driver.find_element(By.ID, "latitude").send_keys("12.3456")
		driver.find_element(By.ID, "longitude").send_keys("-98.7654")
		driver.find_element(By.ID, "authorityEmail").send_keys("sample@email.com")
		driver.find_element(By.ID, "authorityPhone").send_keys("1234567890")
		driver.find_element(By.ID, "password").send_keys("word1234")

		screenshot_file = f"{test_folder}/screenshots/8-super-admin-device_management_cerate_a_device_function-test.png"
		driver.save_screenshot(screenshot_file)
		# Submit the form
		driver.find_element(By.XPATH, "//button[text()='Add Device']").click()

		return True

	except Exception as e:
		return False


def test_super_admin_device_management_delete_a_device_function():

	try:
		remove_icons = driver.find_elements(By.CSS_SELECTOR, "i.fas.fa-trash.fa-2x")
		last_remove_icon = remove_icons[-1]
		last_remove_icon.click()

		screenshot_file = f"{test_folder}/screenshots/9-super-admin-device_management_delete_a_device_function-test.png"
		driver.save_screenshot(screenshot_file)

		alert = driver.switch_to.alert
		alert.accept()

		return True

	except Exception as e:
		return False


def test_super_admin_device_management_edit_a_device_function():


	try:

		edit_icons = driver.find_elements(By.CSS_SELECTOR, "i.fa.fa-pencil-square-o.fa-2x.edit-icon")
		last_edit_icon = edit_icons[-1]
		last_edit_icon.click()

		time.sleep(2)

		driver.find_element(By.ID, "editDeviceName").clear()
		driver.find_element(By.ID, "editDeviceName").send_keys("Edit Name")
		driver.find_element(By.ID, "editLatitude").clear()
		driver.find_element(By.ID, "editLatitude").send_keys("12.34566")
		driver.find_element(By.ID, "editLongitude").clear()
		driver.find_element(By.ID, "editLongitude").send_keys("-98.76545")
		driver.find_element(By.ID, "editAuthorityEmail").clear()
		driver.find_element(By.ID, "editAuthorityEmail").send_keys("editple@email.com")
		driver.find_element(By.ID, "editAuthorityPhone").clear()
		driver.find_element(By.ID, "editAuthorityPhone").send_keys("1234567890")
		driver.find_element(By.ID, "editPassword").clear()
		driver.find_element(By.ID, "editPassword").send_keys("word1234")

		screenshot_file = f"{test_folder}/screenshots/10-super-admin-device_management_edit_a_device_function-test.png"
		driver.save_screenshot(screenshot_file)

		save_changes_button = driver.find_element(By.XPATH, "//button[text()='Save changes']")
		save_changes_button.click()

		return True

	except Exception as e:
		return False


def test_super_admin_settings_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Settings')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/11-super-admin-settings-page-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_super_admin_password_change_function_open():
	try:

		# Enter the current password
		current_password_field = driver.find_element(By.NAME, "current_password")
		current_password_field.send_keys("admin")

		# Enter the new password
		new_password_field = driver.find_element(By.NAME, "new_password")
		new_password_field.send_keys("admin")

		# Confirm the new password
		confirm_password_field = driver.find_element(By.NAME, "confirm_password")
		confirm_password_field.send_keys("admin")

		screenshot_file = f"{test_folder}/screenshots/12-super-admin-password-change-function-test.png"
		driver.save_screenshot(screenshot_file)

		# Click the 'Change' button to submit the form
		change_button = driver.find_element(By.XPATH, "//button[@type='submit']")
		change_button.click()

		return True

	except Exception as e:
		return False

def test_super_admin_logout_function():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Logout')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/13-super-admin-logout_function-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_device_admin_login_failed():

	try:
		# Find the username field by name and enter the value
		username_field = driver.find_element(By.NAME, 'username')
		username_field.send_keys('your_username')

		# Find the password field by name and enter the value
		password_field = driver.find_element(By.NAME, 'password')
		password_field.send_keys('your_password')

		# Find the account_type select element by name and select "Super Admin" option
		account_type_select = Select(driver.find_element(By.NAME, 'account_type'))
		account_type_select.select_by_visible_text('Device Admin')

		# Find the login button by name and click it
		login_button = driver.find_element(By.NAME, 'login')
		login_button.click()
		# Take a screenshot and save it to a file
		screenshot_file = f"{test_folder}/screenshots/13-device-admin-login-failed-test.png"
		driver.save_screenshot(screenshot_file)
		
		return True

	except Exception as e:
		return False

		
def test_device_admin_password_passed():

	try:
		# Find the username field by name and enter the value
		username_field = driver.find_element(By.NAME, 'username')
		username_field.send_keys('test_account')

		# Find the password field by name and enter the value
		password_field = driver.find_element(By.NAME, 'password')
		password_field.send_keys('test123')

		# Find the account_type select element by name and select "Super Admin" option
		account_type_select = Select(driver.find_element(By.NAME, 'account_type'))
		account_type_select.select_by_visible_text('Device Admin')

		# Find the login button by name and click it
		login_button = driver.find_element(By.NAME, 'login')
		login_button.click()
		# Take a screenshot and save it to a file
		screenshot_file = f"{test_folder}/screenshots/14-device-admin-login-passed-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False

def test_device_admin_home_page_open():

	try:

		link = driver.find_element(By.LINK_TEXT, 'Home Page')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/15-device-admin-home-page-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True
	except Exception as e:
		return False


def test_device_admin_data_management_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Data Management')
		link.click()

		# Scroll down the page
		driver.execute_script("window.scrollBy(0, 1000)")

		# Scroll up the page
		driver.execute_script("window.scrollBy(0, -1000)")

		screenshot_file = f"{test_folder}/screenshots/16-device-admin-data-management-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_device_admin_data_management_show_all_data_function():

	try:
		# Find the login button by name and click it
		radio_btn = driver.find_element(By.ID, 'show_all_data')
		radio_btn.click()

		screenshot_file = f"{test_folder}/screenshots/17-device-admin-data-management-show-all-data-function-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_device_admin_device_preferences_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Device Preferences')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/18-device-admin-device-preferences-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False

def test_device_admin_device_preference_edit_a_device_function():
	try:

		time.sleep(2)

		driver.find_element(By.ID, "editDeviceName").clear()
		driver.find_element(By.ID, "editDeviceName").send_keys("Koduwamadu")

		screenshot_file = f"{test_folder}/screenshots/19-device-admin-device_preference_edit_a_device_function-test.png"
		driver.save_screenshot(screenshot_file)

		save_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and text()='Save changes']")
		save_button.click()

		return True

	except Exception as e:
		return False


def test_device_admin_settings_page_open():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Settings')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/20-device-admin-settings-page-view-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False


def test_device_admin_password_change_function():
	try:

		# Enter the current password
		current_password_field = driver.find_element(By.NAME, "current_password")
		current_password_field.send_keys("test123")

		# Enter the new password
		new_password_field = driver.find_element(By.NAME, "new_password")
		new_password_field.send_keys("test123")

		# Confirm the new password
		confirm_password_field = driver.find_element(By.NAME, "confirm_password")
		confirm_password_field.send_keys("test123")

		screenshot_file = f"{test_folder}/screenshots/21-super-admin-password-change-function-test.png"
		driver.save_screenshot(screenshot_file)

		# Click the 'Change' button to submit the form
		change_button = driver.find_element(By.XPATH, "//button[@type='submit']")
		change_button.click()

		return True

	except Exception as e:
		return False

def test_device_admin_logout_function():

	try:
		link = driver.find_element(By.LINK_TEXT, 'Logout')
		link.click()

		screenshot_file = f"{test_folder}/screenshots/13-device-admin-logout_function-test.png"
		driver.save_screenshot(screenshot_file)

		return True

	except Exception as e:
		return False
