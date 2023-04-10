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

    if expected_image == actual_image:
        return True
    else:
        return False

result = test_login_failed()

print(result)