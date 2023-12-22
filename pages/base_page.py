from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Base_page:
    def __init__(self,driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


    def element_is_visible(self,locator,timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elems_are_visble(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))


    def remove_footer(self):
        self.driver.execute_script("document.querySelector('#fixedban').style.display = 'none'")
        self.driver.execute_script("document.querySelector('footer').style.display = 'none'")


