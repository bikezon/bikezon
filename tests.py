import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikezon.settings')
django.setup()
from django.core.exceptions import ObjectDoesNotExist
import logging
from app.models import UserProfile, User, ProductList, Product
from app.forms import UserForm
import unittest
from selenium import webdriver
from selenium import common


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

    def __init__(self):
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
        self.test_signup_fire()
        self.tearDown()


class TestLogIn(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def test_login_fire(self):
        # try to login as user that was just created
        self.driver.get("http://127.0.0.1:8000/login/")
        self.driver.find_element_by_id('id_username').send_keys('TestUser')
        self.driver.find_element_by_id('id_password').send_keys('1234')
        self.driver.find_element_by_id('log-in-button').click()

        # if redirected to home, then successful login, else failed
        if "http://127.0.0.1:8000/" == self.driver.current_url:
            test_logger.info("Sign in and redirect correct")
        else:
            test_logger.warning("Sign in or redirect failed")

    # kill driver on teardown
    def tearDown(self):
        self.driver.quit()

    # setup driver, run the tests and kill the driver
    def run(self):
        self.test_login_fire()
        self.tearDown()


class TestBaseRedirects(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()


    def test_base_redirects(self):
        self.driver.get("http://127.0.0.1:8000/")
        # check login button takes user to login
        self.driver.find_element_by_id('id_login').click()
        if "http://127.0.0.1:8000/login/" == self.driver.current_url:
            test_logger.info("Correct redirect to sign in on base")
        else:
            test_logger.warning("Wrong redirect to sign in on base")

        # go back to main page and try to log out or login and and logout
        self.driver.get("http://127.0.0.1:8000/")
        try:
            self.driver.find_element_by_id('id_logout').click()
        except common.exceptions.NoSuchElementException as e:
            # if cant logut then login and logout
            self.driver.find_element_by_id('id_login').click()
            self.driver.find_element_by_id('id_username').send_keys('TestUser')
            self.driver.find_element_by_id('id_password').send_keys('1234')
            self.driver.find_element_by_id('log-in-button').click()
            self.driver.get("http://127.0.0.1:8000")
            self.driver.find_element_by_id('id_logout').click()

        # check that log redirects to index
        if "http://127.0.0.1:8000/" == self.driver.current_url:
            test_logger.info("Correct redirect from logout")
        else:
            test_logger.warning("Wrong redirect from logout")
        
        # redirect back to home page
        self.driver.get("http://127.0.0.1:8000/")

        # login as test user
        self.driver.find_element_by_id('id_login').click()
        self.driver.find_element_by_id('id_username').send_keys('TestUser')
        self.driver.find_element_by_id('id_password').send_keys('1234')
        self.driver.find_element_by_id('log-in-button').click()

        # go to test user's account to check redirect
        self.driver.find_element_by_id('id_account').click()
        if "http://127.0.0.1:8000/account/" == self.driver.current_url:
            test_logger.info("Correct redirect to account from base")
        else:
            test_logger.warning("Wrong redirect to account from base")
        
            
    
    # kill driver on teardown
    def tearDown(self):
        self.driver.quit()

    # setup driver, run the tests and kill the driver
    def run(self):
        self.test_base_redirects()
        self.tearDown()
    

class TestFollowAndList(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Firefox()

    # kill driver on teardown
    def tearDown(self):
        self.driver.quit()

    # setup driver, run the tests and kill the driver
    def run(self):
        self.test_follow_and_list()
        self.tearDown()

    def test_follow_and_list(self):
        # go to index page
        self.driver.get("http://127.0.0.1:8000/")
        # login as test user
        self.driver.find_element_by_id('id_login').click()
        self.driver.find_element_by_id('id_username').send_keys('TestUser')
        self.driver.find_element_by_id('id_password').send_keys('1234')
        self.driver.find_element_by_id('log-in-button').click()
        # go to index page
        self.driver.get("http://127.0.0.1:8000/")
        # go to bike3 product
        self.driver.find_element_by_id('id_bike3').click()
        # check if redirected to correct page
        if "http://127.0.0.1:8000/product/bike3/" == self.driver.current_url:
            test_logger.info("Correct redirect to product from index")
        else:
            test_logger.warning("Wrong redirect to product from index")

        # add to wish list and follow user
        self.driver.find_element_by_id('id_wishlist').click()
        self.driver.find_element_by_id('id_follow').click()
        user = User.objects.get(username='TestUser')
        user_profile = UserProfile.objects.get(user=user)

        # check that follow worked
        user_to_follow = User.objects.get(username="Dellie")
        profile_to_follow = UserProfile.objects.get(user=user)
        if profile_to_follow in user_profile.follows.all():
            test_logger.info("Following works correctly")
        else:
            test_logger.warning("Following user test failed")

        # check product got added to wish list
        product = Product.objects.get(name="bike3")
        product_list = ProductList.objects.get(user=user_profile)
        if product in product_list.product.all():
            test_logger.info("Adding to wishlist works correctly")
        else:
            test_logger.warning("Adding to wishlist failed")

        # go back to product page
        self.driver.get("http://127.0.0.1:8000/product/bike3/")
        # remove from list and unfollow user
        self.driver.find_element_by_id('id_wishlist').click()
        self.driver.find_element_by_id('id_follow').click()

        # check that unfollowed user
        if not profile_to_follow in user_profile.follows.all():
            test_logger.info("Unfollowing works correctly")
        else:
            test_logger.warning("Unfollowing user test failed")

        # check product got removed from wish list
        if not product in product_list.product.all():
            test_logger.info("Adding to wishlist works correctly")
        else:
            test_logger.warning("Adding to wishlist failed")


# launch tests
if __name__ == '__main__':
    print("Starting all tests, this may take a while...")
    # run registration tests
    print("Testing registartion...")
    test_logger.info("Started registration tests.")
    registration_tester = TestSignup()
    registration_tester.run()
    print("Ok.")
    test_logger.info("All passed.")
    # run login tests
    print("Testing logging in...")
    test_logger.info("Started login tests.")
    login_tester = TestLogIn()
    login_tester.run()
    print("Ok.")
    test_logger.info("All passed.")
    # run base redirect tests
    print("Testing base redirects...")
    test_logger.info("Started base redirect tests.")
    redirect_tester = TestBaseRedirects()
    redirect_tester.run()
    print("Ok.")
    test_logger.info("All passed.")
    # run user following tests
    print("Testing following...")
    test_logger.info("Started following tests.")
    follow_tester = TestFollowAndList()
    follow_tester.run()
    print("Ok.")
    test_logger.info("All passed.")
