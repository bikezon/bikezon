import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')
django.setup()
from selenium import common
from selenium import webdriver
import unittest
from app.forms import UserForm
from app.models import UserProfile, User, ProductList
import logging
from django.core.exceptions import ObjectDoesNotExist

# ----------- Logger config ----------- #
if not os.path.exists("logs/"):
    os.makedirs("logs")

if not os.path.exists("logs/test_logs.log"):
    open("logs/test_logs.log", 'a').close()

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler = logging.FileHandler("logs/test_logs.log")
handler.setFormatter(formatter)
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)
test_logger.addHandler(handler)

# ----------- Tests ----------- #


class TestSignup(unittest.TestCase):
    # param unittest.TestCase: python unit testing library

    def setUp(self):
        self.driver = webdriver.Firefox()

    # localhost firefox registration test
    def test_signup_fire(self):
        """
        uses the gecko driver to create an agent for registration
        if errors arrise see the readme on correct installation of
        gecko drivers.
        """
        test_user_details = {'username': 'TestUser',
                             'email': 'test.user@testemail.com',
                             'password': '1234'}
        # locate sign in page
        self.driver.get("http://127.0.0.1:8000/register/")
        # fill in form
        self.driver.find_element_by_id('id_username').send_keys(
            test_user_details['username'])
        self.driver.find_element_by_id(
            'id_email').send_keys(test_user_details['email'])
        self.driver.find_element_by_id('id_password').send_keys(
            test_user_details['password'])
        self.driver.find_element_by_id('id_verify_password').send_keys(
            test_user_details['password'])
        # try to register with picture
        try:
            self.driver.find_element_by_id(
                "id_picture").send_keys("test_img.png")
        except common.exceptions.InvalidArgumentException as e:
            pass

        self.driver.find_element_by_id('id_phone_0').send_keys("981773")
        self.driver.find_element_by_id('id_phone_1').send_keys("44")
        self.driver.find_element_by_id('submit').click()

        # check correct redirection
        if "http://127.0.0.1:8000/register/" == self.driver.current_url:
            test_logger.info("Correct redirect after registration")
        else:
            test_logger.warning("Incorrect redirect noticed")
            print(self.driver.current_url)

        # check that new user object and profile exist
        try:
            test_user = User.objects.get(
                username=test_user_details['username'])
            test_user_profile = UserProfile.objects.get(user=test_user)
            test_logger.info("User registered correctly")
        except ObjectDoesNotExist:
            test_logger.warning("User registered incorrectly")
            self.tearDown()
            print(e)

        # test if users wishlists get created when registering
        try:
            test_user_list = ProductList.objects.get(
                user=test_user_profile or None)
            test_logger.info("User wish list created correctly")
        except ObjectDoesNotExist:
            test_logger.warning(
                "Did not create user wish list on registration")
            self.tearDown()
            print(e)

    # kill driver on teardown
    def tearDown(self):
        self.driver.quit()

    # setup driver, run the tests and kill the driver
    def run(self):
        self.setUp()
        self.test_signup_fire()
        self.tearDown()


# launch tests
if __name__ == '__main__':
    sign_up_test = TestSignup()
    sign_up_test.run()
