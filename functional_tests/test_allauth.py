
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.test import RequestFactory
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured
import os, sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate


class TestGoogleLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='sammy', email='s@g.com', password='123')

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.live_server_url = cls.server_url
                return

        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def tearDown(self):
        self.browser.quit()

    def get_env_variable(self, var_name):
        try:
            return os.environ[var_name]
        except KeyError:
            error_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(error_msg)

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
            (By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
            (By.ID, element_id)))

    def get_button_by_class(self, element_class):
        return self.browser.wait.until(EC.element_to_be_clickable(
            (By.Class, element_class)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def user_login(self):
        import json
        with open("taskbuster/fixtures/google_user.json") as f:
            credentials = json.loads(f.read())
        print (self.get_element_by_id("Email"))
        self.get_element_by_id("Email").send_keys(credentials["Email"])
        self.get_button_by_id("next").click()
        print (self.get_element_by_id("Passwd"))
        self.get_element_by_id("Passwd").send_keys(credentials["Passwd"])
        for btn in ["signIn", "submit_approve_access"]:
            self.get_button_by_id(btn).click()
        return

    def environment_login(self):
        username = self.get_env_variable('username')
        password = self.get_env_variable('password')
        self.get_element_by_id("id_login").send_keys(username)
        self.get_element_by_id("id_password").send_keys(password)
        self.get_button_by_class("primaryAction").click()

    def test_email_login(self):
        self.browser.get(self.get_full_url("home"))
        google_login = self.get_element_by_id("google_login")
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("logout")
        self.assertEqual(
            google_login.get_attribute("href"),
            self.live_server_url + "/accounts/login")
        google_login.click()
        self.environment_login()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("google_login")
        google_logout = self.get_element_by_id("logout")
        google_logout.click()
        google_login = self.get_element_by_id("google_login")
