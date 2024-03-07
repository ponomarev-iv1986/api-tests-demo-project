import time

import pytest

from api_requests import pprb_request
from models.pprb_models.universal_open_legal_account import (
    UniversalOpenLegalAccount,
)
from resources.pprb_resources import status, status_list
from resources.pprb_resources.request_input_data import (
    universal_open_legal_account,
)


@pytest.fixture(scope='module')
def uola() -> UniversalOpenLegalAccount:
    return UniversalOpenLegalAccount(pprb_request.send_uola)


class TestUniversalOpenLegalAccount:
    @pytest.fixture(scope='class', autouse=True)
    def send_requests(self, uola):
        uola.send_identification(
            **universal_open_legal_account.uola_identification
        )
        print(universal_open_legal_account.uola_identification)
        # time.sleep(10)
        # uola.send_generate_doc(**universal_open_legal_account.uola_generate_doc)
        # time.sleep(10)
        # uola.send_open_account(**universal_open_legal_account.uola_open_account)
        # time.sleep(60)

    def test_1(self, uola):
        status_code = uola.response_identification.status_code
        headers = uola.response_identification.headers
        body = uola.response_identification.json()
        print(status_code, end='\n\n')
        print(headers, end='\n\n')
        print(
            uola.response_identification.request.body.decode('utf-8'),
            end='\n\n',
        )
        print(body)


'''
Просто пример теста на другой метод:

# class TestStatus700StatusProcessSigningComplete:
#     @pytest.fixture(scope='class', autouse=True)
#     def send_request(self, pprb):
#         pprb.send_request(
#             **open_legal_account_status.status_700_status_process_signing_complete
#         )
#
#     def test_verify_status_code(self, pprb):
#         pprb.verify_status_code(200)
#
#     @pytest.mark.parametrize(
#         'key, value',
#         [
#             pytest.param('RqUID', 'TBD', id='RqUID'),
#             pytest.param('SpName', None, id='SpName'),
#             pytest.param('RqTm', None, id='RqTm'),
#         ],
#     )
#     def test_verify_headers(self, pprb, key, value):
#         pprb.verify_headers(key, value)
#
#     def test_validate_json_schema(self, pprb):
#         pprb.validate_json_schema('open_legal_account_status.json')
#
#     def test_verify_status(self, pprb):
#         pprb.verify_status(**status.success_700)
#
#     def test_verify_status_process(self, pprb):
#         pprb.verify_status_process('signingComplete')
'''
