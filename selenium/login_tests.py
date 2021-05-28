import pytest
from login_to_ya import login_to_ya
from settings import login, password, extended_result

class TestLoginYa:

    def setup(self):
        self.login = login
        self.password = password
        self.extended_result = extended_result
        print('Setup')

    def test_login_ya(self):
        assert login_to_ya(self.login, self.password) == self.extended_result

    def teardown(self):
        print('Teardown')