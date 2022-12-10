import time

import allure
from seleniumbase import BaseCase
import pytest
from behave import step
from pytest_bdd import scenarios, given, when, then


class test_ca(BaseCase):
    login_field = "//*[@id='email']"
    password_field = "//*[@id='password']"

    @allure.title("test for login")
    def test_swag_labs(self):
        self.open("https://aimaidhelp.com/login")
        self.type(self.login_field, text='vburmich@apro.ai')
        self.type(self.password_field, text='1111')
        self.click("//*[text()='Log In']")
        a = 'awdawd'
        self.assert_title('AI Maid Help')
        print("test")




