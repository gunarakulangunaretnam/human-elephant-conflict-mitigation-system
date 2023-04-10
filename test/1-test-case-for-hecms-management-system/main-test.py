import os
import time
import utilities
from jinja2 import Template
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


test_folder = f"results/{datetime.now().strftime('%Y-%m-%d')}-{datetime.now().strftime('%H-%M-%S')}-results"
os.mkdir(test_folder) 
os.mkdir(f"{test_folder}/screenshots") 

utilities.test_folder = test_folder

test_run_start_time = datetime.now().strftime('%H:%M:%S')

super_admin_results = {
    "super_admin_failed_login_test": utilities.test_super_admin_login_failed(),
    "super_admin_passed_password_test": utilities.test_super_admin_password_passed(),
    "super_admin_home_page_view_test": utilities.test_super_admin_home_page_open(),
    "super_admin_home_page_filter_search_test": utilities.test_super_admin_home_page_filter(),
    "super_admin_data_management_page_view_test": utilities.test_super_admin_data_management_page_open(),
    "super_admin_data_management_show_all_data_search_test": utilities.test_super_admin_data_management_show_all_data_function(),
    "super_admin_device_management_page_view_test": utilities.test_super_admin_device_management_page_open(),
    "super_admin_device_management_create_device_test": utilities.test_super_admin_device_management_create_a_device_function(),
    "super_admin_device_management_edit_device_test": utilities.test_super_admin_device_management_edit_a_device_function(),
    "super_admin_device_management_delete_device_test": utilities.test_super_admin_device_management_delete_a_device_function(),
    "super_admin_settings_page_view_test": utilities.test_super_admin_settings_page_open(),
    "super_admin_password_change_page_view_test": utilities.test_super_admin_password_change_function_open(),
    "super_admin_logout_test": utilities.test_super_admin_logout_function()
}

device_admin_results = {
    "device_admin_failed_login_test": utilities.test_device_admin_login_failed(),
    "device_admin_passed_password_test": utilities.test_device_admin_password_passed(),
    "device_admin_home_page_view_test": utilities.test_device_admin_home_page_open(),
    "device_admin_data_management_page_view_test": utilities.test_device_admin_data_management_page_open(),
    "device_admin_data_management_show_all_data_search_test": utilities.test_device_admin_data_management_show_all_data_function(),
    "device_admin_device_preferences_page_view_test": utilities.test_device_admin_device_preferences_page_open(),
    "device_admin_device_preference_edit_device_test": utilities.test_device_admin_device_preference_edit_a_device_function(),
    "device_admin_settings_page_view_test": utilities.test_device_admin_settings_page_open(),
    "device_admin_password_change_page_view_test": utilities.test_device_admin_password_change_function(),
    "device_admin_logout_test": utilities.test_device_admin_logout_function()
}

# Loop through super_admin_results dictionary and capitalize keys and store as "Passed" or "Failed"
for key in list(super_admin_results.keys()):
    capitalized_key = key.replace('_', ' ').title()
    super_admin_results[capitalized_key] = "Passed" if super_admin_results[key] else "Failed"
    super_admin_results.pop(key)

# Loop through device_admin_results dictionary and capitalize keys and store as "Passed" or "Failed"
for key in list(device_admin_results.keys()):
    capitalized_key = key.replace('_', ' ').title()
    device_admin_results[capitalized_key] = "Passed" if device_admin_results[key] else "Failed"
    device_admin_results.pop(key)


test_run_end_time = datetime.now().strftime('%H:%M:%S')

template = Template('''
<!DOCTYPE html>
<html>

<head>
    <title>HECMS Management System Testing Results</title>
    <!-- Include Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>

<body>
    <div class="container mt-5">
        <h1 class="text-center">HECMS Management System Testing Results</h1>
        <h6 class="text-center">Test Run: {{test_run_date}} | {{test_run_start_time}} - {{test_run_end_time}}</h6>
        <hr>

        <br>

        <h3 style="text-align:center !important;">Super Admin Test Results</h3>
        
        <br>

        <table class="table table-bordered table-hover">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Result</th>
                </tr>
            </thead>
            <tbody>
                <!-- Loop through the super admin test results -->
                {% for test_name, result in super_admin_results.items() %}
                <tr>
                    <td>{{ test_name }}</td>
                    <td>{{ result }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <br>

        <h3 style="text-align:center !important;">Device Admin Test Results</h3>
        
        <br>

        <table class="table table-bordered table-hover">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Result</th>
                </tr>
            </thead>
            <tbody>
                <!-- Loop through the device admin test results -->
                {% for test_name, result in device_admin_results.items() %}
                <tr>
                    <td>{{ test_name }}</td>
                    <td>{{ result }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

       
    </div>

    <!-- Include Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>

</html>
''')

# Render the template with the data
html = template.render(test_run_start_time = test_run_start_time, test_run_date = datetime.now().strftime('%Y-%m-%d'),  test_run_end_time=test_run_end_time, super_admin_results=super_admin_results, device_admin_results=device_admin_results)

# Write the rendered HTML to a file
with open(f'{test_folder}/test_results.html', 'w') as f:
    f.write(html)



