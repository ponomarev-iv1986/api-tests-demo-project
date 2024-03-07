import pytest

from api_requests import pprb_request
from models.pprb_models.update_info_for_roa_model import UpdateInfoForROA
from resources.pprb_resources import status
from resources.pprb_resources.request_input_data import update_info_for_roa


@pytest.fixture(scope='module')
def uifr():
    return UpdateInfoForROA(pprb_request.send)


class TestStatus703:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, uifr):
        uifr.send_request(**update_info_for_roa.status_703)

    def test_verify_status_code(self, uifr):
        uifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, uifr, key, value):
        uifr.verify_headers(key, value)

    def test_validate_json_schema(self, uifr):
        uifr.validate_json_schema('update_info_for_roa.json')

    def test_verify_status(self, uifr):
        uifr.verify_status(**status.success_703)


class TestStatus702:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, uifr):
        uifr.send_request(**update_info_for_roa.status_702)

    def test_verify_status_code(self, uifr):
        uifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, uifr, key, value):
        uifr.verify_headers(key, value)

    def test_validate_json_schema(self, uifr):
        uifr.validate_json_schema('update_info_for_roa.json')

    def test_verify_status(self, uifr):
        uifr.verify_status(**status.tech_error_702)


class TestStatus704:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, uifr):
        uifr.send_request(**update_info_for_roa.status_704)

    def test_verify_status_code(self, uifr):
        uifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, uifr, key, value):
        uifr.verify_headers(key, value)

    def test_validate_json_schema(self, uifr):
        uifr.validate_json_schema('update_info_for_roa.json')

    def test_verify_status(self, uifr):
        uifr.verify_status(**status.tech_error_704)


class TestStatusMinus20:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, uifr):
        uifr.send_request(**update_info_for_roa.status_minus20)

    def test_verify_status_code(self, uifr):
        uifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, uifr, key, value):
        uifr.verify_headers(key, value)

    def test_validate_json_schema(self, uifr):
        uifr.validate_json_schema('update_info_for_roa.json')

    def test_verify_status(self, uifr):
        uifr.verify_status(**status.tech_error_minus_20)


class TestStatusMinus40:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, uifr):
        uifr.send_request(**update_info_for_roa.status_minus40)

    def test_verify_status_code(self, uifr):
        uifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, uifr, key, value):
        uifr.verify_headers(key, value)

    def test_validate_json_schema(self, uifr):
        uifr.validate_json_schema('update_info_for_roa.json')

    def test_verify_status(self, uifr):
        uifr.verify_status(**status.tech_error_minus_40)
