from settings import login_xpath, uname_xpath, passw_xpath, lsend_xpath, username, password
from time import sleep
from selenium.webdriver.common.by import By


def login_functions(self):
    self.driver.get('https://www.neobux.com')
    sleep(1.5)
    log_btn = self.driver.find_element(By.XPATH, login_xpath)
    log_btn.click()
    while "m/l/?vl=" not in self.driver.current_url:
        sleep(0.1)
    sleep(1.5)
    usern = self.driver.find_element(By.XPATH, uname_xpath)
    usern.send_keys(username)
    passc = self.driver.find_element(By.XPATH, passw_xpath)
    passc.send_keys(password)
    html = self.driver.page_source
    if "Código de Verificação" in html or "Verification Code" in html:
        print("Жду когда ты пройдёшь капчу и залогинишся")
    else:
        print("Капчи нет, делаю всё сам")
        send_btn = self.driver.find_element(By.XPATH, lsend_xpath)
        send_btn.click()
    while "c/?vl=" not in self.driver.current_url:
        sleep(0.1)
    sleep(1.5)
