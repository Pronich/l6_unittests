import accounting
import pytest


class TestAccountingPytest:
    def setup(self):
        print('method setup')

    @pytest.mark.parametrize("doc_number,expected", [('2207 876234', True), ('12345', False)])
    def test_check_doc(self, doc_number, expected):
        assert accounting.check_doc(doc_number) == expected

    @pytest.mark.parametrize("doc_number, expected", [('2207 876234', 0), ('12345', False)])
    def test_check_doc_index(self, doc_number, expected):
        assert accounting.check_doc_index(doc_number) == expected

    @pytest.mark.parametrize("doc_number, expected", [('2207 876234', '1'), ('12345', None)])
    def test_get_shelf(self, doc_number, expected):
        assert accounting.get_shelf(doc_number) == expected

    @pytest.mark.parametrize("new_shelf, expected", [('2', True), ('10', False)])
    def test_check_shelf(self, new_shelf, expected):
        assert accounting.check_shelf(new_shelf) == expected

    @pytest.mark.parametrize("doc_number, new_shelf, expected", [('12345', '1', ('12345', '1', True)), ('22234', '2', ('22234', '2', True))])
    def test_update_doc_in_shelf(self, doc_number, new_shelf, expected):
        assert accounting.update_doc_in_shelf(doc_number, new_shelf) == expected

    def test_get_name(self, mocker):
        mocker.patch(
            'accounting.input_doc_number',
            return_value='2207 876234'
        )
        assert accounting.get_name() == 'Василий Гупкин'

    def test_get_doc_shelf(self, mocker):
        mocker.patch(
            'accounting.input_doc_number',
            return_value='2207 876234'
        )
        assert accounting.get_doc_shelf() == '1'

    def test_get_doc_list(self):
        expected = [{'2207 876234', 'passport', 'Василий Гупкин'},
                    {'Геннадий Покемонов', '11-2', 'invoice'},
                    {'10006', 'insurance', 'Аристарх Павлов'}]

        assert accounting.get_doc_list() == expected

    def test_add_new_doc(self, mocker):
        test_param=["12345","passport","Василий Пупкин","10"]
        mocker.patch('builtins.input', side_effect=test_param)
        expected = ({'type': 'passport', 'number': '12345', 'name': 'Василий Пупкин'}, ('10', ['12345']))
        assert accounting.add_new_doc() == expected

    def test_delete_doc(self, mocker):
        mocker.patch(
            'accounting.input_doc_number',
            return_value='2207 876234'
        )
        assert accounting.delete_doc() == ('2207 876234', True)

    def test_change_doc_shelf(self, mocker):
        mocker.patch(
            'accounting.input_doc_number',
            return_value='10006'
        )
        mocker.patch(
            'accounting.get_new_shelf',
            return_value='15'
        )
        assert accounting.change_doc_shelf() == ('15', ['10006'])

    def test_add_new_shelf(self, mocker):
        mocker.patch(
            'accounting.get_new_shelf',
            return_value='20'
        )
        expected = 'Новая полка успешно создана'
        assert accounting.add_new_shelf() == expected

    def teardown(self):
        print('method teardown')
