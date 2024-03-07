import pytest

from api_requests import pprb_request
from models.pprb_models.get_info_for_roa_model import GetInfoForROA
from resources.pprb_resources import status
from resources.pprb_resources.request_input_data import get_info_for_roa


@pytest.fixture(scope='module')
def gifr():
    return GetInfoForROA(pprb_request.send)


class TestStatus701StatusProcessOk:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_701_status_process_ok)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_701_ok.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.success_701)

    def test_verify_status_process(self, gifr):
        gifr.verify_status_process_in('infoSentToClient', 'clientClickOnLink')


class TestStatus701StatusProcessFailed:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_701_status_process_failed)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_701_failed.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.success_701)

    def test_verify_status_process(self, gifr):
        gifr.verify_status_process_not_in(
            'infoSentToClient', 'clientClickOnLink'
        )


class TestStatus702:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_702)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_702.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.tech_error_702)


class TestStatusMinus20:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_minus_20)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_minus_20.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.tech_error_minus_20)


class TestStatusMinus30:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_minus_30)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_minus_30.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.tech_error_minus_30)


class TestStatusMinus40:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, gifr):
        gifr.send_request(**get_info_for_roa.status_minus_40)

    def test_verify_status_code(self, gifr):
        gifr.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
        ],
    )
    def test_verify_headers(self, gifr, key, value):
        gifr.verify_headers(key, value)

    def test_validate_json_schema(self, gifr):
        gifr.validate_json_schema('get_info_for_roa_minus_40.json')

    def test_verify_status(self, gifr):
        gifr.verify_status(**status.tech_error_minus_40)
