import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')
django.setup()
from selenium import common
from selenium import webdriver
import unittest
from app.forms import UserForm
import django

########## Testing Forms ##########


class TestSignup(unittest.TestCase):
    """
        :param unittest.TestCase: python unit testing library
    """

    def setUp(self):
        self.driver = webdriver.Firefox()

    # localhost firefox registration test
    def test_signup_fire(self):
            """
            uses the gecko driver to create an agent for registration
            if errors arrise see the readme on correct installation of
            gecko drivers.

            """   
        # locate sign in page
        self.driver.get("http://127.0.0.1:8000/register/")
        # fill in form
        self.driver.find_element_by_id('id_username').send_keys("TestUser")
        self.driver.find_element_by_id(
            'id_email').send_keys("test.user@testemail.com")
        self.driver.find_element_by_id('id_password').send_keys("1234")
        self.driver.find_element_by_id('id_verify_password').send_keys("1234")
        # try to register with picture
        try:
            self.driver.find_element_by_id("id_picture").send_keys("test_img.png")
        except common.exceptions.InvalidArgumentException as e:
            pass

        self.driver.find_element_by_id('id_phone_0').send_keys("981773")
        self.driver.find_element_by_id('id_phone_1').send_keys("44")
        self.driver.find_element_by_id('submit').click()

        # check correct redirection
        self.assertIn("http://127.0.0.1:8000/register/",
                      self.driver.current_url)

    # kill driver on teardown
    def tearDown(self):
        self.driver.quit
    
    # setup driver, run the tests and kill the driver
    def run(self):
        self.setUp()
        self.test_signup_fire()
        self.tearDown()


########## Testing Views ##########


########## Testing Models ##########


########## Misc Tests ##########


# launch tests
if __name__ == '__main__':
    sign_up_test = TestSignup()
    sign_up_test.run()
