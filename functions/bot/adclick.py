from settings import ads_xpath
from time import sleep


def adclick_functions(self):
    ads = self.driver.find_element_by_xpath(ads_xpath)
    ads.click()
    while "m/v/?vl=" not in self.driver.current_url:
        sleep(0.1)
    sleep(1.5)
    i = 1
    html = self.driver.page_source
    adc = 0
    finder = str(html).find("/v/?a=")
    if finder != -1:
        while True:
            finder = str(html).find("/v/?a=", finder)
            if finder == -1:
                break
            else:
                adc += 1
                finder += 1
        while True:
            if i <= int(adc):
                ad = self.driver.find_element_by_xpath('//*[@id="l0l' + str(i) + '"]')
                ad = ad.find_element_by_xpath('//*[@id="da' + str(i) + 'a"]')
                if ad.find_element_by_xpath('//*[@id="tg_' + str(i) + '"]').get_attribute("class") \
                        .split().count("adf") > 0:
                    ad.click()
                    sleep(1)
                    adr = self.driver.find_element_by_xpath('//*[@id="l' + str(i) + '"]')
                    adr.click()
                    sleep(28)
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    sleep(1)
                else:
                    i += 1
            else:
                break
    else:
        print("Реклам на сегодня не найдено")
