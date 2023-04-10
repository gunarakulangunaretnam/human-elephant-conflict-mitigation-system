import time
import pyautogui


test_folder = ""


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

    expected_image = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-login-failed-expected.png')
    actual_image = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-login-failed-actual.png')

    pyautogui.press('enter')

    if expected_image == actual_image:
        return True
    else:
        return False

    

def test_login_succeed(): # Test Login Failed

    # Wait for the login window to open
    time.sleep(3)

    # Press TAB to focus on the username textbox
    pyautogui.press('tab')

    # Type the username
    pyautogui.typewrite("test_account")

    # Press TAB to focus on the password textbox
    pyautogui.press('tab')

    # Type the password
    pyautogui.typewrite("test123")

    # Press TAB to focus on the login button
    pyautogui.press('tab')

    # Press SPACE to click the login button

    image1 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-login-succeed-image1.png')

    pyautogui.press('space')

    time.sleep(1)

    image2 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-login-succeed-image2.png')

    if image1 == image2:
        return False
    else:
        return True


def test_select_video_and_start_processing():
    # Press Tab four times
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    # Press Space once
    pyautogui.press('space')

    # Press Tab once
    pyautogui.press('tab')

    pyautogui.typewrite("assets/video/sample-test-video.m4v")

    time.sleep(1)

    # Click the "start-processing-button.png" image
    button_location = pyautogui.locateCenterOnScreen('assets\\start-processing-button.png')
    pyautogui.click(button_location)

    image1 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-camera-open-image1.png')

    time.sleep(10)

    image2 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-camera-open-image2.png')

    if image1 == image2:
        return False
    else:
        return True


def test_alarm_options():
    time.sleep(1)

    # Click the "start-processing-button.png" image
    button_location = pyautogui.locateCenterOnScreen('assets\\alarm-off-on.png')
    pyautogui.click(button_location)

    time.sleep(2)

    return True



def test_stop_processing():

    time.sleep(2)

    image1 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-stop-processing-image1.png')

    # Click the "start-processing-button.png" image
    button_location = pyautogui.locateCenterOnScreen('assets\\stop-processing-button.png')
    pyautogui.click(button_location)
    time.sleep(1)

    image2 = pyautogui.screenshot(f'{test_folder}\\screenshots\\test-stop-processing-image2.png')


    if image1 == image2:
        return False
    else:
        return True


