import pytest
from conftest import driver
from pages.form_page import Fillpage
class Testformpage():
    def test_form(self,driver):
        form_page = Fillpage(driver,'https://demoqa.com/automation-practice-form')
        form_page.open()
        form_page.remove_footer()
        name, lastname, email = form_page.fill()
        result = form_page.get_result()
        print(name , lastname , email)
        print(result)
        assert 1==1

