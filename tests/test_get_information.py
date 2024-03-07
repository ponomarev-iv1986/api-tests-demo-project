import pytest

from api_requests import base_request
from models.project_models.get_information_model import GetInformation
from resources.project_resources import status
from resources.project_resources.request_input_data import get_information


@pytest.fixture(scope='module')
def get_info() -> GetInformation:
    return GetInformation(base_request.send)


class TestStatusCompleted:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, get_info):
        get_info.send_request(**get_information.get_information_completed)

    def test_verify_status_code(self, get_info):
        get_info.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('uid', 'TBD', id='UID'),
            pytest.param('name', None, id='Name'),
        ],
    )
    def test_verify_headers(self, get_info, key, value):
        get_info.verify_headers(key, value)

    def test_validate_json_schema(self, get_info):
        get_info.validate_json_schema('get_information_json_schema.json')

    def test_verify_status(self, get_info):
        get_info.verify_status(**status.status_completed)


class TestStatusFailed:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, get_info):
        get_info.send_request(**get_information.get_information_failed)

    def test_verify_status_code(self, get_info):
        get_info.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('uid', 'TBD', id='UID'),
            pytest.param('name', None, id='Name'),
        ],
    )
    def test_verify_headers(self, get_info, key, value):
        get_info.verify_headers(key, value)

    def test_validate_json_schema(self, get_info):
        get_info.validate_json_schema('get_information_json_schema.json')

    def test_verify_status(self, get_info):
        get_info.verify_status(**status.status_failed)
