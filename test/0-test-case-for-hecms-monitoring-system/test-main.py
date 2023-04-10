import pyautogui
import time


def test_login_failed(): # Test Login Failed

    # Wait for the login window to open
    time.sleep(5)

    # Press TAB to focus on the username textbox
    pyautogui.press('tab')

    # Type the username
    pyautogui.typewrite("my_username")

    # Press TAB to focus on the password textbox
    pyautogui.press('tab')

    # Type the password
    pyautogui.typewrite("my_password")

    # Press TAB to focus on the login button
    pyautogui.press('tab')

    # Press SPACE to click the login button
    pyautogui.press('space')

    time.sleep(3)

    expected_image = pyautogui.screenshot('temp\\test-login-failed-expected.png')
    actual_image = pyautogui.screenshot('temp\\test-login-failed-actual.png')

    pyautogui.press('enter')

    if expected_image == actual_image:
        return True
    else:
        return False

    

def test_login_succeed(): # Test Login Failed

    # Wait for the login window to open
    time.sleep(5)

    # Press TAB to focus on the username textbox
    pyautogui.press('tab')

    # Type the username
    pyautogui.typewrite("64315b0a75")

    # Press TAB to focus on the password textbox
    pyautogui.press('tab')

    # Type the password
    pyautogui.typewrite("device2")

    # Press TAB to focus on the login button
    pyautogui.press('tab')

    # Press SPACE to click the login button

    image1 = pyautogui.screenshot('temp\\test-login-succeed-image1.png')

    pyautogui.press('space')

    time.sleep(1)

    image2 = pyautogui.screenshot('temp\\test-login-succeed-image2.png')

    if image1 == image2:
        return False
    else:
        return True



def test_camera_opened_and_start_processing():
    # Press Tab twice
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')

    # Press Space once
    pyautogui.press('space')

    # Press Tab once
    pyautogui.press('tab')

    # Press the down arrow once
    pyautogui.press('down')

    # Press Enter
    pyautogui.press('enter')

    # Click the "start-processing-button.png" image
    button_location = pyautogui.locateCenterOnScreen('assets\\start-processing-button.png')
    pyautogui.click(button_location)

    image1 = pyautogui.screenshot('temp\\test-camera-open-image1.png')

    time.sleep(12)

    image2 = pyautogui.screenshot('temp\\test-camera-open-image2.png')

    if image1 == image2:
        return False
    else:
        return True


def test_stop_processing():
    pass
test_login_failed()
test_login_succeed()
result = test_camera_opened_and_start_processing()

print(result)
