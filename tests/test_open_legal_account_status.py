import pytest

from api_requests import pprb_request
from models.pprb_models.open_legal_account_status import OpenLegalAccountStatus
from resources.pprb_resources import status, status_list
from resources.pprb_resources.request_input_data import (
    open_legal_account_status,
)


@pytest.fixture(scope='module')
def olas():
    return OpenLegalAccountStatus(pprb_request.send)


class TestStatus700StatusProcessSigningComplete:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_700_status_process_signing_complete
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('signingComplete')


class TestStatus700StatusProcessAccountOpened:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_700_status_process_account_opened
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('accountOpened')


class TestStatusProcessRejectStatusList1012:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1012
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1012)


class TestStatusProcessRejectStatusList1018:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1018
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1018)


class TestStatusProcessRejectStatusList1020:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1020
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1020)


class TestStatusProcessRejectStatusList1021:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1021
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1021)


class TestStatusProcessRejectStatusList1022:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1022
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1022)


class TestStatusProcessRejectStatusList1027:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(
            **open_legal_account_status.status_process_reject_status_list_1027
        )

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status_reject.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.success_700)

    def test_verify_status_process(self, olas):
        olas.verify_status_process('reject')

    def test_verify_status_list(self, olas):
        olas.verify_status_list(**status_list.reject_1027)


class TestStatusMinus20:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(**open_legal_account_status.status_minus_20)

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.tech_error_minus_20)


class TestStatusMinus40:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(**open_legal_account_status.status_minus_40)

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.tech_error_minus_40)


class TestStatus104:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(**open_legal_account_status.status_104)

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.tech_error_104)


class TestStatus204:
    @pytest.fixture(scope='class', autouse=True)
    def send_request(self, olas):
        olas.send_request(**open_legal_account_status.status_204)

    def test_verify_status_code(self, olas):
        olas.verify_status_code(200)

    @pytest.mark.parametrize(
        'key, value',
        [
            pytest.param('RqUID', 'TBD', id='RqUID'),
            pytest.param('SpName', None, id='SpName'),
            pytest.param('RqTm', None, id='RqTm'),
        ],
    )
    def test_verify_headers(self, olas, key, value):
        olas.verify_headers(key, value)

    def test_validate_json_schema(self, olas):
        olas.validate_json_schema('open_legal_account_status.json')

    def test_verify_status(self, olas):
        olas.verify_status(**status.tech_error_204)
