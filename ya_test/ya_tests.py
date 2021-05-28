from yaLoader import yaUpLoader
import pytest
from settings import ya_token

class TestYaDisc:

    def setup(self):
        self.yad = yaUpLoader(ya_token)
        print('method setup')

    @pytest.mark.parametrize('path, extended', [('netology/netology1', (200, 'disk:/netology/netology1')), ('netology/netology2', (200, 'disk:/netology/netology2'))])
    def test_create_check_folder(self, path, extended):
        self.path = path
        self.yad.create_folder(path)
        assert self.yad.check_folder(path) == extended

    def test_fail_check_folder(self):
        with pytest.raises(Exception):
            self.path = 'netology/failtests'
            self.yad.create_folder(self.path)
            assert self.yad.check_folder('netology/truetest') == (200, 'disk:/netology/netology1')

    def teardown(self):
        self.yad.delete_folder(self.path)
        print('method teardown')