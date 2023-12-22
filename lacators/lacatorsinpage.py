from selenium.webdriver.common.by import By
from random import randint

class Frompagelacators():
    FirstName = (By.ID,'firstName')
    LastName = (By.ID,'lastName')
    Email = (By.ID,'userEmail')
    Gender = (By.CSS_SELECTOR, f'[for="gender-radio-1"]')
    Number = (By.ID, 'userNumber')
    Subject = (By.ID, "subjectsInput")
    Hobbies = (By.CSS_SELECTOR, f'[for="hobbies-checkbox-1"]')
    FileInput = (By.ID, 'uploadPicture')
    Address = (By.ID, 'currentAddress')
    Submit = (By.ID, 'submit')
    Result = (By.XPATH, '//div[@class="table-responsive"]//td[2]')