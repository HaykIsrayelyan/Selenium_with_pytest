import time

from pages.base_page import Base_page
from lacators.lacatorsinpage import Frompagelacators as Lacators


class Fillpage(Base_page):
    def fill(self):
        name = 'Hayko'
        lastname = 'Israyelyan'
        email = 'haykoisrayelyan18@mail.ru'
        number = 12345671444
        subject = 'subject'
        address = 'YEREVAN ARMENIA '


        self.element_is_visible(Lacators.FirstName).send_keys(name)

        self.element_is_visible(Lacators.LastName).send_keys(lastname)
        self.element_is_visible(Lacators.Email).send_keys(email)
        self.element_is_visible(Lacators.Gender).click()
        self.element_is_visible(Lacators.Number).send_keys(number)
        self.element_is_visible(Lacators.Subject).send_keys(subject)
        self.element_is_visible(Lacators.Hobbies).click()
        self.element_is_visible(Lacators.FileInput).send_keys(r'C:\Users\User\PycharmProjects\QA project\pages\tut.txt')
        self.element_is_visible(Lacators.Address).send_keys(address)
        self.element_is_visible(Lacators.Submit).click()
        time.sleep(5)

        return name,lastname,email


    def get_result(self):
        result_List = self.elems_are_visble(Lacators.Result)
        result_text = [i.text for i in result_List]
        return result_text
