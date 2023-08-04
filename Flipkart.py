import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)


@pytest.mark.usefixtures("driver_init")
class Flipkart_Test:
    pass



class Test_Flipkart_login(Flipkart_Test):
    def test_login(self):
        pop_up = self.driver.find_element(By.CSS_SELECTOR, "._3wFoIb.row")
        popup_close = self.driver.find_element(By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
        time.sleep(4)
        if pop_up.is_displayed():
            popup_close.click()
            assert True
        else:
            print("pop up is not showing")
            assert False
        time.sleep(50)
        login_button = self.driver.find_element(By.CSS_SELECTOR, "._1_3w1N")
        if login_button.is_displayed() and login_button.is_enabled():
            print("login button is displayed")
            login_button.click()
            assert True
        else:
            print("login button is not displayed")
            assert False
        mobile_number = self.driver.find_element(By.CSS_SELECTOR, "._2IX_2-.VJZDxU")
        mobile_number.send_keys("7288920277")
        time.sleep(3)
        request_otp_button = self.driver.find_element(By.CSS_SELECTOR, "._2KpZ6l._2HKlqd._3AWRsL")
        if request_otp_button.is_displayed() and request_otp_button.is_enabled():
            print("request OTP button is displayed and enabled")
            assert True
            request_otp_button.click()
        else:
            print("request OTP button is displayed or enabled")
            assert False
        time.sleep(10)
        message = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Please enter the OTP sent to')]")
        if message.is_displayed():
            assert True
        else:
            assert False
