from time import sleep
from settings import adprize_xpath
from selenium.webdriver.common.by import By


def adprize_functions(self):
    i = 0
    adprize_text = str(int(self.driver.find_element(By.XPATH, adprize_xpath).text) + 1)
    while True:
        if i != int(adprize_text):
            self.driver.find_element(By.XPATH, adprize_xpath).click()
            print(f'Получаю приз {str(i + 1)}из {adprize_text}')
            sleep(10)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            i += 1
        elif i == int(adprize_text):
            break
