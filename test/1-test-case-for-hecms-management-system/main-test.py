import os
import time
import utilities
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


test_folder = f"results/{datetime.now().strftime('%Y-%m-%d')}-{datetime.now().strftime('%H-%M-%S')}-results"
os.mkdir(test_folder) 
os.mkdir(f"{test_folder}/screenshots") 

utilities.test_folder = test_folder

utilities.test_super_admin_password_failed()
utilities.test_super_admin_password_failed()
utilities.test_super_admin_password_failed()

# Wait for user input before closing the browser window
input("Press Enter to close the browser window...")
driver.quit()


